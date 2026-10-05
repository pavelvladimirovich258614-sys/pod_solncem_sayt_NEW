#!/usr/bin/env python3
"""kupit-tyr request backend: "Заказать звонок", "Напишите нам" and "Круизы".

Validates a submission (name + phone, plus a message for the two write-us forms) and relays it by e-mail directly to the
recipient's MX (no external service, no stored secrets, nothing is written to disk except a
log line without personal data). Listens on 127.0.0.1 only; nginx proxies /api/callback to it.

Settings are constants below. The LEAD_* environment variables exist only for tests
(local port, log file, fake SMTP server); the systemd unit does not set them.
"""

import hashlib
import json
import logging
import os
import re
import smtplib
import threading
import time
import unicodedata
from collections import defaultdict, deque
from datetime import datetime, timedelta, timezone
from email.message import EmailMessage
from email.utils import format_datetime, make_msgid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

LISTEN_HOST = "127.0.0.1"
LISTEN_PORT = int(os.environ.get("LEAD_PORT", "8731"))
LOG_PATH = os.environ.get("LEAD_LOG", "/var/log/kupit-tyr-lead/app.log")

MAIL_TO = "coralclub5av@mail.ru"
MAIL_FROM = "noreply@kupit-tyr.ru"
HELO_NAME = "kupit-tyr.ru"
RECIPIENT_DOMAIN = MAIL_TO.split("@", 1)[1]
# tests only: "host:port" of a local fake SMTP server (skips the MX lookup)
TEST_SMTP = os.environ.get("LEAD_TEST_SMTP")

ALLOWED_ORIGINS = {"https://kupit-tyr.ru", "https://www.kupit-tyr.ru"}
if os.environ.get("LEAD_TEST_ORIGIN"):
    ALLOWED_ORIGINS.add(os.environ["LEAD_TEST_ORIGIN"])

SEND_PER_IP = 3              # accepted requests per IP per window
SEND_WINDOW = 15 * 60
INVALID_PER_IP = 20          # rejected requests per IP per window (keeps validation cheap for bots)
SEND_GLOBAL_PER_HOUR = 30    # hard cap on mails to the manager per hour
DUPLICATE_WINDOW = 10 * 60   # the same phone inside this window is answered "ok" but not mailed again
MIN_FILL_SECONDS = 2         # a human needs more than this between opening the form and sending it
MAX_BODY = 7000          # 1500 four-byte characters in a message still fit; nginx stops anything over 8k
MAX_DRAIN = 16384

NAME_MIN, NAME_MAX = 2, 60
MESSAGE_MAX = 1500
MESSAGE_REQUIRED_MIN = 3
MAX_LINKS = 2
# topic -> (mail subject, heading line of the mail body, is the message required)
TOPICS = {
    "callback": ("Заказ звонка с сайта kupit-tyr.ru", "Заказ обратного звонка с сайта kupit-tyr.ru", False),
    "write": ("Напишите нам: сообщение с сайта kupit-tyr.ru", "Сообщение с сайта kupit-tyr.ru: форма «Напишите нам»", True),
    "cruise": ("Круизы: заявка с сайта kupit-tyr.ru", "ИНТЕРЕС: КРУИЗЫ. Обращение из карточки «Круизы» на сайте kupit-tyr.ru", False),
}
PHONE_CHARS_RE = re.compile(r"^[\d\s()+\-]{5,25}$")
MSK = timezone(timedelta(hours=3))

log = logging.getLogger("callback")

_lock = threading.Lock()
_send_hits = defaultdict(deque)
_invalid_hits = defaultdict(deque)
_global_hits = deque()
_recent_phones = {}
_pending = set()  # phones whose mail is being delivered right now


class SendFailed(Exception):
    pass


def _trim(dq, now, window):
    while dq and now - dq[0] > window:
        dq.popleft()


def check_invalid_budget(ip, now=None):
    """True if this IP may still make (possibly invalid) requests."""
    now = now or time.time()
    with _lock:
        dq = _invalid_hits[ip]
        _trim(dq, now, SEND_WINDOW)
        return len(dq) < INVALID_PER_IP


def note_invalid(ip, now=None):
    now = now or time.time()
    with _lock:
        _invalid_hits[ip].append(now)


def reserve_send(ip, phone_key, now=None):
    """Returns 'ok' (slot taken), 'pending' (same phone is being sent right now), 'duplicate' or 'limited'."""
    now = now or time.time()
    with _lock:
        for k in [k for k, t in _recent_phones.items() if now - t > DUPLICATE_WINDOW]:
            del _recent_phones[k]
        if phone_key in _pending:
            return "pending"
        if phone_key in _recent_phones:
            return "duplicate"
        dq = _send_hits[ip]
        _trim(dq, now, SEND_WINDOW)
        _trim(_global_hits, now, 3600)
        if len(dq) >= SEND_PER_IP or len(_global_hits) >= SEND_GLOBAL_PER_HOUR:
            return "limited"
        dq.append(now)
        _global_hits.append(now)
        _recent_phones[phone_key] = now
        _pending.add(phone_key)
        return "ok"


def finish_send(phone_key):
    with _lock:
        _pending.discard(phone_key)


def release_send(ip, phone_key):
    """Give the slot back when the mail could not be sent, so the visitor may retry at once."""
    with _lock:
        _pending.discard(phone_key)
        _recent_phones.pop(phone_key, None)
        if _send_hits[ip]:
            _send_hits[ip].pop()
        if _global_hits:
            _global_hits.pop()


def clean_name(raw):
    s = re.sub(r"\s+", " ", str(raw)).strip()
    return s


def clean_message(raw):
    s = str(raw).replace("\r\n", "\n").replace("\r", "\n")
    s = "".join(ch for ch in s if ch == "\n" or unicodedata.category(ch) != "Cc")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def dedupe_key(fields):
    return "|".join((fields["topic"], fields["phone"], hashlib.sha256(fields["message"].encode()).hexdigest()[:12]))


def validate_name(name):
    if not (NAME_MIN <= len(name) <= NAME_MAX):
        return "Укажите имя (от 2 до 60 символов)."
    letters = 0
    for ch in name:
        cat = unicodedata.category(ch)
        if cat.startswith("L"):
            letters += 1
        elif ch not in " -.'’":
            return "В имени допустимы только буквы, пробел и дефис."
    if letters < 2:
        return "Укажите имя (от 2 до 60 символов)."
    return None


def normalize_phone(raw):
    """Returns (normalized '+7XXXXXXXXXX' style string, None) or (None, error)."""
    s = str(raw).strip()
    if not PHONE_CHARS_RE.match(s):
        return None, "Укажите телефон в правильном формате, например +7 900 000-00-00."
    plus = s.startswith("+")
    digits = re.sub(r"\D", "", s)
    if not plus and len(digits) == 11 and digits[0] in "78":
        digits = "7" + digits[1:]
        plus = True
    elif not plus and len(digits) == 10 and digits[0] == "9":
        digits = "7" + digits
        plus = True
    if not (10 <= len(digits) <= 15) or len(set(digits)) < 3:
        return None, "Укажите телефон в правильном формате, например +7 900 000-00-00."
    if digits[0] == "7" and len(digits) != 11:
        return None, "Укажите телефон в правильном формате, например +7 900 000-00-00."
    return "+" + digits, None


def validate(payload):
    """Returns (fields, None) or (None, (field, message))."""
    if not isinstance(payload, dict):
        return None, ("form", "Некорректные данные формы.")
    topic = payload.get("topic", "callback")
    if not isinstance(topic, str) or topic not in TOPICS:
        return None, ("form", "Некорректные данные формы.")
    name = clean_name(payload.get("name", ""))
    err = validate_name(name)
    if err:
        return None, ("name", err)
    phone, err = normalize_phone(payload.get("phone", ""))
    if err:
        return None, ("phone", err)
    message = ""
    if topic != "callback":
        raw = payload.get("message", "")
        if not isinstance(raw, str):
            return None, ("message", "Некорректный текст сообщения.")
        message = clean_message(raw)
        if len(message) > MESSAGE_MAX:
            return None, ("message", "Сообщение слишком длинное (не больше %d символов)." % MESSAGE_MAX)
        if TOPICS[topic][2] and len(message) < MESSAGE_REQUIRED_MIN:
            return None, ("message", "Напишите сообщение.")
        if len(re.findall(r"https?://|www\.", message, re.I)) > MAX_LINKS:
            return None, ("message", "В сообщении слишком много ссылок.")
    if payload.get("consent") is not True:
        return None, ("consent", "Нужно согласие на обработку персональных данных.")
    return {"topic": topic, "name": name, "phone": phone, "message": message}, None


def honeypot_filled(payload):
    """The hidden field is invisible to people; only a form-filling bot touches it."""
    return bool(str(payload.get("hp_field", "")).strip())


def too_fast(payload):
    """Sent sooner than a person can fill the form (or the timer value is missing/garbled)."""
    try:
        return float(payload.get("elapsed", 0)) < MIN_FILL_SECONDS * 1000
    except (TypeError, ValueError):
        return True


def format_phone(p):
    d = p[1:]
    if d.startswith("7") and len(d) == 11:
        return "+7 (%s) %s-%s-%s" % (d[1:4], d[4:7], d[7:9], d[9:11])
    return p


def build_message(fields):
    now = datetime.now(MSK)
    subject, heading, _ = TOPICS[fields["topic"]]
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = MAIL_FROM
    msg["To"] = MAIL_TO
    msg["Date"] = format_datetime(now)
    msg["Message-ID"] = make_msgid(domain="kupit-tyr.ru")
    body = "%s\n\nИмя: %s\nТелефон: %s\n" % (heading, fields["name"], format_phone(fields["phone"]))
    if fields["topic"] != "callback":
        body += "Сообщение:\n%s\n\n" % (fields["message"] or "(без текста)")
    body += "Время заявки: %s (МСК)\n\n" % now.strftime("%d.%m.%Y %H:%M")
    body += ("Клиент дал согласие на обработку персональных данных на сайте. "
             "Свяжитесь с ним по указанному телефону в рабочее время.\n")
    msg.set_content(body)
    return msg


def mx_hosts():
    if TEST_SMTP:
        host, port = TEST_SMTP.rsplit(":", 1)
        return [(host, int(port))]
    import dns.resolver  # only needed in production

    answers = dns.resolver.resolve(RECIPIENT_DOMAIN, "MX", lifetime=8)
    hosts = sorted(((r.preference, str(r.exchange).rstrip(".")) for r in answers), key=lambda x: x[0])
    return [(h, 25) for _, h in hosts]


def deliver(msg):
    """Hands the message to the recipient's MX. Returns the receiving server's final reply
    (queue id, no personal data) so that the log proves the server accepted it."""
    last = None
    for host, port in mx_hosts():
        try:
            with smtplib.SMTP(host, port, local_hostname=HELO_NAME, timeout=10) as smtp:
                smtp.ehlo(HELO_NAME)
                if smtp.has_extn("starttls"):
                    smtp.starttls()
                    smtp.ehlo(HELO_NAME)
                smtp.mail(MAIL_FROM)
                code, resp = smtp.rcpt(MAIL_TO)
                if code not in (250, 251):
                    raise smtplib.SMTPRecipientsRefused({MAIL_TO: (code, resp)})
                code, resp = smtp.data(msg.as_bytes())
                if code != 250:
                    raise smtplib.SMTPDataError(code, resp)
                reply = resp.decode("utf-8", "replace").strip()
            return "%s %s [%s]" % (code, reply, host)
        except Exception as exc:  # try the next MX host
            last = exc
    raise SendFailed(type(last).__name__ if last else "no MX host reachable")


def send_callback(fields):
    msg = build_message(fields)
    try:
        return deliver(msg)
    except SendFailed:
        time.sleep(2)  # one more try for a transient failure
        return deliver(msg)


def ip_tag(ip):
    return hashlib.sha256(ip.encode()).hexdigest()[:8]


class Handler(BaseHTTPRequestHandler):
    server_version = "kupit-tyr-callback/2.0"
    timeout = 10  # a stalled client cannot hold a thread

    def log_message(self, fmt, *args):
        pass  # the default access log would repeat the raw request line

    def _client_ip(self):
        return (self.headers.get("X-Real-IP") or self.client_address[0]).split(",")[0].strip()

    def _json(self, status, payload):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        self._json(405, {"ok": False, "error": "method not allowed"})

    do_PUT = do_DELETE = do_PATCH = do_GET

    def do_POST(self):
        try:
            self._handle_post()
        except Exception as exc:  # never leave the client without an answer
            log.error("callback result=internal_error error=%s", type(exc).__name__)
            try:
                self._json(500, {"ok": False, "error": "Внутренняя ошибка. Позвоните нам."})
            except Exception:
                pass

    def _handle_post(self):
        # read the declared body first: answering and closing with unread data resets the connection for the client
        try:
            length = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            length = 0
        raw = self.rfile.read(length) if 0 < length <= MAX_BODY else b""
        if MAX_BODY < length <= MAX_DRAIN:
            self.rfile.read(length)  # too big to use, but still consumed (nginx already stops anything over 8k)

        if self.path != "/api/callback":
            self._json(404, {"ok": False, "error": "not found"})
            return
        ip = self._client_ip()
        tag = ip_tag(ip)

        origin = self.headers.get("Origin")
        if origin is not None and origin not in ALLOWED_ORIGINS:
            log.info("callback ip=%s result=bad_origin", tag)
            self._json(403, {"ok": False, "error": "forbidden"})
            return
        if not (self.headers.get("Content-Type") or "").lower().startswith("application/json"):
            self._json(415, {"ok": False, "error": "unsupported media type"})
            return
        if length <= 0 or length > MAX_BODY:
            self._json(400, {"ok": False, "error": "bad request"})
            return

        if not check_invalid_budget(ip):
            log.info("callback ip=%s result=rate_limited_invalid", tag)
            self._json(429, {"ok": False, "error": "Слишком много попыток. Попробуйте позже или позвоните нам."})
            return
        try:
            payload = json.loads(raw.decode("utf-8"))
        except Exception:
            note_invalid(ip)
            log.info("callback ip=%s result=bad_json", tag)
            self._json(400, {"ok": False, "error": "Некорректные данные формы."})
            return

        if isinstance(payload, dict) and honeypot_filled(payload):
            note_invalid(ip)
            log.info("callback ip=%s result=spam_dropped", tag)
            # answer like a success: the bot learns nothing, nothing is mailed
            self._json(200, {"ok": True})
            return

        fields, err = validate(payload)
        if err:
            note_invalid(ip)
            log.info("callback ip=%s result=validation_failed field=%s", tag, err[0])
            self._json(422, {"ok": False, "field": err[0], "error": err[1]})
            return

        if too_fast(payload):
            note_invalid(ip)
            log.info("callback ip=%s result=too_fast", tag)
            self._json(422, {"ok": False, "field": "form", "error": "Проверьте данные и нажмите «Отправить заявку» ещё раз."})
            return

        key = dedupe_key(fields)
        slot = reserve_send(ip, key)
        if slot == "pending":
            log.info("callback ip=%s result=pending", tag)
            self._json(409, {"ok": False, "error": "Заявка уже отправляется. Подождите несколько секунд."})
            return
        if slot == "duplicate":
            log.info("callback ip=%s result=duplicate", tag)
            self._json(200, {"ok": True})  # already passed to the manager a moment ago
            return
        if slot == "limited":
            log.info("callback ip=%s result=rate_limited", tag)
            self._json(429, {"ok": False, "error": "Слишком много заявок. Попробуйте позже или позвоните нам."})
            return

        try:
            reply = send_callback(fields)
        except Exception as exc:
            release_send(ip, key)
            log.warning("callback ip=%s result=send_failed error=%s", tag, type(exc).__name__)
            self._json(502, {"ok": False, "error": "Не удалось отправить заявку. Попробуйте ещё раз или позвоните нам."})
            return

        finish_send(key)
        log.info("callback ip=%s topic=%s result=sent smtp=%s", tag, fields["topic"], reply)
        self._json(200, {"ok": True})


def main():
    logging.basicConfig(filename=LOG_PATH, level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    ThreadingHTTPServer((LISTEN_HOST, LISTEN_PORT), Handler).serve_forever()


if __name__ == "__main__":
    main()
