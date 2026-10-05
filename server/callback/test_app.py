"""Tests for the callback backend. Run: python -m unittest server/callback/test_app.py -v
A fake SMTP server on a local port stands in for the recipient's MX: nothing leaves this machine."""
import email
import email.policy
import json
import os
import socketserver
import sys
import tempfile
import threading
import time
import unittest
import urllib.error
import urllib.request

os.environ["LEAD_TEST_ORIGIN"] = "http://127.0.0.1"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

MAILS = []
SMTP_MODE = {"fail": False}


class FakeSMTP(socketserver.StreamRequestHandler):
    def _w(self, s):
        self.wfile.write((s + "\r\n").encode())

    def handle(self):
        if SMTP_MODE["fail"]:
            self._w("421 busy")
            return
        self._w("220 fake ESMTP")
        data_mode, buf, rcpt = False, [], []
        while True:
            line = self.rfile.readline()
            if not line:
                return
            if data_mode:
                if line == b".\r\n":
                    MAILS.append({"rcpt": list(rcpt), "body": b"".join(buf).decode("utf-8", "replace")})
                    data_mode = False
                    self._w("250 2.0.0 Ok: queued as TESTQ123")
                else:
                    buf.append(line)
                continue
            cmd = line.decode().strip().upper()
            if cmd.startswith("EHLO") or cmd.startswith("HELO"):
                self._w("250 fake")
            elif cmd.startswith("MAIL FROM"):
                self._w("250 ok")
            elif cmd.startswith("RCPT TO"):
                rcpt.append(line.decode().strip())
                self._w("250 ok")
            elif cmd == "DATA":
                data_mode = True
                self._w("354 go")
            elif cmd == "QUIT":
                self._w("221 bye")
                return
            else:
                self._w("250 ok")


class QuietTCP(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


def start_backend():
    smtp = QuietTCP(("127.0.0.1", 0), FakeSMTP)
    threading.Thread(target=smtp.serve_forever, daemon=True).start()
    os.environ["LEAD_TEST_SMTP"] = "127.0.0.1:%d" % smtp.server_address[1]
    import app

    app.TEST_SMTP = os.environ["LEAD_TEST_SMTP"]
    app.time.sleep = lambda s: None  # no 2 s pause before the retry in tests
    logfile = os.path.join(tempfile.mkdtemp(), "app.log")
    import logging

    logging.basicConfig(filename=logfile, level=logging.INFO, format="%(message)s", force=True)
    from http.server import ThreadingHTTPServer

    srv = ThreadingHTTPServer(("127.0.0.1", 0), app.Handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    return app, srv, smtp, logfile


APP, SRV, SMTP, LOGFILE = start_backend()
URL = "http://127.0.0.1:%d/api/callback" % SRV.server_address[1]


def post(payload, headers=None, raw=None, ip="203.0.113.9"):
    h = {"Content-Type": "application/json", "X-Real-IP": ip, "Origin": "http://127.0.0.1"}
    h.update(headers or {})
    data = raw if raw is not None else json.dumps(payload).encode()
    req = urllib.request.Request(URL, data=data, headers={k: v for k, v in h.items() if v is not None}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read())


def good(**kw):
    d = {"name": "Анна", "phone": "+7 900 123-45-67", "consent": True, "hp_field": "", "elapsed": 8000}
    d.update(kw)
    return d


class Base(unittest.TestCase):
    def setUp(self):
        MAILS.clear()
        SMTP_MODE["fail"] = False
        for d in (APP._send_hits, APP._invalid_hits):
            d.clear()
        APP._global_hits.clear()
        APP._recent_phones.clear()
        APP._pending.clear()


class ValidationUnit(Base):
    def test_phone_normalisation(self):
        n = APP.normalize_phone
        self.assertEqual(n("8 (900) 123-45-67")[0], "+79001234567")
        self.assertEqual(n("+7 900 123 45 67")[0], "+79001234567")
        self.assertEqual(n("9001234567")[0], "+79001234567")
        self.assertEqual(n("+995 555 12 34 56")[0], "+995555123456")
        for bad in ["", "123", "abcdefghij", "+7 900 123", "1111111111", "+7 (900) 123-45-6700", "<script>", "+7 900 123-45-67; DROP"]:
            self.assertIsNone(n(bad)[0], bad)

    def test_name(self):
        v = APP.validate_name
        for ok in ["Анна", "Анна-Мария", "Ли", "John O'Neil", "Иван Петров"]:
            self.assertIsNone(v(ok), ok)
        for bad in ["", "А", "x" * 61, "http://spam.ru", "a@b.ru", "Анна123", "<b>x</b>", "1234"]:
            self.assertIsNotNone(v(bad), bad)


class Endpoint(Base):
    def test_valid_request_is_mailed_once_to_approved_address(self):
        code, body = post(good())
        self.assertEqual((code, body), (200, {"ok": True}))
        self.assertEqual(len(MAILS), 1)
        m = MAILS[0]
        self.assertIn("coralclub5av@mail.ru", m["rcpt"][0])
        parsed = email.message_from_string(m["body"], policy=email.policy.default)
        self.assertEqual(parsed["Subject"], "Заказ звонка с сайта kupit-tyr.ru")
        self.assertEqual(parsed["To"], "coralclub5av@mail.ru")
        self.assertTrue(parsed["Date"].endswith("+0300"))
        text = parsed.get_content()
        self.assertIn("Имя: Анна", text)
        self.assertIn("Телефон: +7 (900) 123-45-67", text)

    def test_validation_errors_name_the_field(self):
        cases = [
            (good(name=""), "name"),
            (good(name="http://x.ru"), "name"),
            (good(phone="12"), "phone"),
            (good(phone=""), "phone"),
            (good(consent=False), "consent"),
            (good(consent="true"), "consent"),
        ]
        for payload, field in cases:
            code, body = post(payload)
            self.assertEqual(code, 422, payload)
            self.assertEqual(body["field"], field)
        self.assertEqual(MAILS, [])

    def test_bad_input(self):
        self.assertEqual(post(None, raw=b"not json")[0], 400)
        self.assertEqual(post(None, raw=b"")[0], 400)
        self.assertEqual(post(None, raw=b"x" * 5000)[0], 400)
        self.assertEqual(post([1, 2, 3])[0], 422)
        self.assertEqual(post(None, raw=b'"str"')[0], 422)
        self.assertEqual(post(good(), headers={"Content-Type": "text/plain"})[0], 415)
        self.assertEqual(post(good(), headers={"Origin": "https://evil.example"})[0], 403)
        self.assertEqual(MAILS, [])

    def test_header_injection_is_rejected(self):
        code, body = post(good(name="Анна\r\nBcc: spam@example.com"))
        self.assertEqual((code, body["field"]), (422, "name"))
        self.assertEqual(MAILS, [])

    def test_wrong_method_and_path(self):
        req = urllib.request.Request(URL, method="GET")
        with self.assertRaises(urllib.error.HTTPError) as cm:
            urllib.request.urlopen(req, timeout=5)
        self.assertEqual(cm.exception.code, 405)
        req = urllib.request.Request(URL.replace("callback", "lead"), data=b"{}", headers={"Content-Type": "application/json"}, method="POST")
        with self.assertRaises(urllib.error.HTTPError) as cm:
            urllib.request.urlopen(req, timeout=5)
        self.assertEqual(cm.exception.code, 404)

    def test_honeypot_is_silent_and_not_mailed(self):
        self.assertEqual(post(good(hp_field="http://spam"))[0:2], (200, {"ok": True}))
        self.assertEqual(MAILS, [])

    def test_too_fast_asks_to_retry_instead_of_losing_the_lead(self):
        code, body = post(good(elapsed=300))
        self.assertEqual((code, body["field"]), (422, "form"))
        code, _ = post(good(elapsed="abc"))
        self.assertEqual(code, 422)
        self.assertEqual(MAILS, [])
        self.assertEqual(post(good())[0], 200)  # the retry goes through
        self.assertEqual(len(MAILS), 1)

    def test_duplicate_phone_is_not_mailed_twice(self):
        self.assertEqual(post(good())[0], 200)
        self.assertEqual(post(good(name="Анна П."), ip="198.51.100.7")[0], 200)  # even from another address
        self.assertEqual(len(MAILS), 1)
        self.assertEqual(post(good(phone="8 900 765 43 21"))[0], 200)
        self.assertEqual(len(MAILS), 2)

    def test_same_phone_while_sending_is_pending_not_success(self):
        self.assertEqual(APP.reserve_send("1.1.1.1", "+79000000001"), "ok")
        self.assertEqual(APP.reserve_send("2.2.2.2", "+79000000001"), "pending")
        APP.release_send("1.1.1.1", "+79000000001")  # the first send failed: the retry may go
        self.assertEqual(APP.reserve_send("2.2.2.2", "+79000000001"), "ok")
        APP.finish_send("+79000000001")  # the first send succeeded: later copies are duplicates
        self.assertEqual(APP.reserve_send("3.3.3.3", "+79000000001"), "duplicate")

    def test_rate_limit_per_ip(self):
        for i in range(3):
            self.assertEqual(post(good(phone="+7 900 111-22-3%d" % i))[0], 200)
        self.assertEqual(post(good(phone="+7 900 111-22-39"))[0], 429)
        self.assertEqual(len(MAILS), 3)
        self.assertEqual(post(good(phone="+7 900 111-22-40"), ip="198.51.100.20")[0], 200)  # others unaffected

    def test_invalid_budget(self):
        codes = [post(good(phone="1"))[0] for _ in range(22)]
        self.assertEqual(codes[:20], [422] * 20)
        self.assertEqual(codes[20:], [429, 429])

    def test_global_hourly_cap(self):
        for i in range(30):
            self.assertEqual(post(good(phone="+7 901 000-00-%02d" % (i + 10)), ip="10.0.0.%d" % i)[0], 200)
        self.assertEqual(post(good(phone="+7 902 000-00-01"), ip="10.0.1.1")[0], 429)
        self.assertEqual(len(MAILS), 30)

    def test_smtp_failure_gives_502_and_frees_the_slot(self):
        SMTP_MODE["fail"] = True
        code, body = post(good())
        self.assertEqual(code, 502)
        self.assertIn("позвоните", body["error"])
        SMTP_MODE["fail"] = False
        self.assertEqual(post(good())[0], 200)  # same phone may retry immediately
        self.assertEqual(len(MAILS), 1)

    def test_log_has_no_personal_data(self):
        post(good(name="Секретное Имя", phone="+7 900 555-44-33"))
        with open(LOGFILE, encoding="utf-8") as f:
            logging_text = f.read()
        for s in ["Секретное", "900 555", "9005554433", "203.0.113.9"]:
            self.assertNotIn(s, logging_text)
        self.assertIn("result=sent smtp=250 2.0.0 Ok: queued as TESTQ123", logging_text)


def parsed(i=-1):
    return email.message_from_string(MAILS[i]["body"], policy=email.policy.default)


class Topics(Base):
    def test_write_us_is_mailed_with_message(self):
        code, body = post(good(topic="write", message="Хочу в Грузию в ноябре,\r\nна двоих.  Какие варианты?"))
        self.assertEqual((code, body), (200, {"ok": True}))
        m = parsed()
        self.assertEqual(m["Subject"], "Напишите нам: сообщение с сайта kupit-tyr.ru")
        self.assertEqual(m["To"], "coralclub5av@mail.ru")
        text = m.get_content()
        self.assertIn("форма «Напишите нам»", text)
        self.assertIn("Телефон: +7 (900) 123-45-67", text)
        self.assertIn("Сообщение:\nХочу в Грузию в ноябре,\nна двоих. Какие варианты?", text)
        self.assertNotIn("КРУИЗ", text)

    def test_cruise_mail_states_the_interest_explicitly(self):
        self.assertEqual(post(good(topic="cruise", message="Средиземное море, июнь"))[0], 200)
        m = parsed()
        self.assertTrue(m["Subject"].startswith("Круизы:"))
        text = m.get_content()
        self.assertIn("ИНТЕРЕС: КРУИЗЫ", text)
        self.assertIn("Средиземное море, июнь", text)

    def test_cruise_message_is_optional_write_message_is_required(self):
        self.assertEqual(post(good(topic="cruise", message=""))[0], 200)
        self.assertIn("(без текста)", parsed().get_content())
        for msg in ["", "  ", "ab"]:
            code, body = post(good(topic="write", message=msg, phone="+7 900 555-66-7%d" % len(msg)))
            self.assertEqual((code, body["field"]), (422, "message"), msg)

    def test_callback_ignores_a_message_and_keeps_its_old_shape(self):
        self.assertEqual(post(good(message="должно быть проигнорировано"))[0], 200)
        text = parsed().get_content()
        self.assertEqual(parsed()["Subject"], "Заказ звонка с сайта kupit-tyr.ru")
        self.assertNotIn("проигнорировано", text)
        self.assertNotIn("Сообщение:", text)
        self.assertNotIn("КРУИЗ", text)

    def test_message_validation(self):
        for payload, field in [
            (good(topic="write", message="x" * 1501), "message"),
            (good(topic="write", message=["список"]), "message"),
            (good(topic="write", message=None), "message"),
            (good(topic="write", message="http://a.ru http://b.ru www.c.ru купите"), "message"),
            (good(topic="write", message="Здравствуйте", consent=False), "consent"),
            (good(topic="write", message="Здравствуйте", name=""), "name"),
            (good(topic="write", message="Здравствуйте", phone="1"), "phone"),
        ]:
            code, body = post(payload)
            self.assertEqual((code, body.get("field")), (422, field), payload)
        self.assertEqual(MAILS, [])

    def test_unknown_topic_is_rejected(self):
        for t in ["spam", "", None, 1, ["write"]]:
            code, body = post(good(topic=t, message="Здравствуйте"))
            self.assertEqual((code, body["field"]), (422, "form"), t)
        self.assertEqual(MAILS, [])

    def test_one_link_in_a_message_is_fine(self):
        self.assertEqual(post(good(topic="write", message="Нашёл тур: https://example.com/tour"))[0], 200)

    def test_control_characters_are_removed(self):
        self.assertEqual(post(good(topic="write", message="Привет\x00\x07 мир\n\n\n\nконец"))[0], 200)
        self.assertIn("Привет мир\n\nконец", parsed().get_content())

    def test_same_phone_different_topics_are_all_delivered(self):
        self.assertEqual(post(good())[0], 200)
        self.assertEqual(post(good(topic="write", message="Вопрос по визе"))[0], 200)
        self.assertEqual(post(good(topic="cruise", message="Круиз по Волге"))[0], 200)
        self.assertEqual(len(MAILS), 3)
        # an exact repeat is still a duplicate, a different message from the same person is not
        self.assertEqual(post(good(topic="write", message="Вопрос по визе"))[0], 200)
        self.assertEqual(len(MAILS), 3)

    def test_long_message_with_four_byte_characters_fits(self):
        # the browser sends raw UTF-8 (JSON.stringify), not \u escapes
        raw = json.dumps(good(topic="write", message="😀" * 1500), ensure_ascii=False).encode("utf-8")
        self.assertGreater(len(raw), 6000)
        code, _ = post(None, raw=raw)
        self.assertEqual(code, 200)

    def test_log_names_the_topic_without_personal_data(self):
        post(good(topic="cruise", message="Секретный маршрут", name="Скрытое Имя"))
        with open(LOGFILE, encoding="utf-8") as f:
            text = f.read()
        self.assertIn("topic=cruise result=sent", text)
        for needle in ["Секретный", "Скрытое"]:
            self.assertNotIn(needle, text)


if __name__ == "__main__":
    unittest.main()
