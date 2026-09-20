# Варианты деплоя сайта «Под Солнцем»

**Дата:** 19.09.2026 (UTC+08).
**Что деплоим:** статический сайт `D:\ТУРИЗМ СЕРГЕЙ\07_CODE\site-pod-solncem\dist\` (610 КБ, 16 страниц, Astro 5 + Tailwind v4 + MDX + sitemap).
**Требования (из задачи):** opensource / self-hosted / free tier; доступ из РФ без VPN; страница < 3 сек до interactive; Lighthouse mobile ≥ 90.
**Ниже — 2 валидных варианта (по запросу RZA), с детальным сравнением.**

---

## Вариант A. Managed PaaS (Netlify / Vercel / Cloudflare Pages — free tier)

### Что это
Подключаем `site-pod-solncem` репозиторий (или конкретный `dist/`) к одному из managed-хостингов для статических сайтов. Хостинг сам билдит, отдаёт через глобальный CDN, выпускает Let's Encrypt-сертификат, настраивает домен.

### Подварианты (что выбирать внутри A)

| Хостинг | Free tier | CDN | Astro-поддержка | DNS-пропагация | SSL | PR preview |
|---|---|---|---|---|---|---|
| **Netlify** | 100 GB bandwidth/мес, 300 build-мин | Global Edge (~50+ PoP) | нативная, `netlify.toml` уже написан | 5–30 мин (после CNAME) | авто Let's Encrypt | да |
| Vercel | 100 GB bandwidth/мес | Global Edge | нативная | 5–30 мин | авто | да |
| Cloudflare Pages | unlimited bandwidth, 500 билдов/мес | Cloudflare (250+ PoP, **включая RU/СНГ**) | через `@astrojs/cloudflare` или static | 5–30 мин | авто | да |
| GitHub Pages | 100 GB bandwidth/мес | GitHub CDN (нет в RU) | static через `gh-pages` | 5–60 мин | авто | нет |

### Рекомендация Raekwon (Э1 GZA + Э9 уточнение)

- **Основной — Netlify.** Архитектура `SITE_ARCHITECTURE.md § 5.3` уже зафиксировала Netlify как приоритет. `netlify.toml` в `07_CODE/site-pod-solncem/` готов (security headers, cache-control, build env NODE_VERSION=22). One-click deploy.
- **Запасной №1 — Cloudflare Pages.** У Cloudflare CDN сильнее в РФ (есть PoP в Москве/СПб/Казани), что улучшает метрику «доступ из РФ без VPN, страница < 3 сек». Минус: билды чуть медленнее, и придётся дописать `wrangler.toml` (или взять `@astrojs/cloudflare` адаптер, переключить `output: 'static'` остаётся — static build).
- **Запасной №2 — Vercel.** Подходит, но не лучший для Astro (Vercel first-class только с Next.js).

### Что нужно от Павла для запуска варианта A

1. **Если Netlify:** `NETLIFY_AUTH_TOKEN` (Personal Access Token из https://app.netlify.com/user/applications#personal-access-tokens). Либо сказать «создай новый сайт через UI и пришли site-id» — тогда я не трогаю токены и деплою через webhook/CLI в его аккаунт.
2. **Если Cloudflare:** `CLOUDFLARE_API_TOKEN` + `CLOUDFLARE_ACCOUNT_ID`. Либо «создай проект в dashboard и пришли project-name».
3. **Если Vercel:** `VERCEL_TOKEN` + `VERCEL_ORG_ID` + `VERCEL_PROJECT_ID`. Аналогично.
4. **Домен** — выбранный из `domains-shortlist.md`, оплаченный и с известным регистратором.
5. **DNS-доступ** — у регистратора домена. Либо Павел сам прописывает A/CNAME, либо я делаю через API регистратора (нужен `REGRU_API_TOKEN` или аналог, **обязательно отдельным токеном с минимальной зоной**).

### Acceptance criteria для варианта A

- ✅ `https://<chosen-domain>/` → 200 OK, главная с лого + Her + Daisy-Wave + 5 destinations + 4 tours + manager + reviews + CTA.
- ✅ `https://<chosen-domain>/sitemap-index.xml` → 200 OK, реальный XML.
- ✅ `https://<chosen-domain>/robots.txt` → 200 OK, разрешает индексацию.
- ✅ Cookie-баннер виден на первом заходе, после `localStorage.ps_cookie_consent === 'accepted'` не повторяется.
- ✅ CTA ведут на `https://t.me/pod_solncem_travel_bot?start=<source>` (12 уникальных меток).
- ✅ Из РФ (Москва, через российский прокси или VPN-tools как Pagespeed+RuMetric) — TTFB < 300 мс, LCP < 2.5 сек, Lighthouse mobile ≥ 90.
- ✅ `www.<chosen-domain>` → 301 на bare (или наоборот, по решению Павла).

### Стоимость

0 ₽/мес (free tier при условии < 100 GB bandwidth и < 30 build-мин/день для Netlify/Vercel; для Cloudflare Pages — безлимит по bandwidth). При превышении — апгрейд за деньги (до 19$/мес за Pro у Netlify, у Cloudflare — pay-as-you-go).

### Сложность для меня как для Raekwon

- **Низкая.** `netlify deploy --prod --dir=dist --site=<id>` или `vercel deploy --prod` или `wrangler pages deploy dist`. Плюс правка DNS (1 A-запись + 1 CNAME для www).
- **Время:** 30 минут от получения токенов до live-сайта (если DNS уже есть).

---

## Вариант B. Self-hosted (VPS Павла на reg.ru / домашний сервер)

### Что это
Поднимаем на уже оплаченном VPS `pod-solncem.ru` (там же, где живёт Telegram-бот и Mini App) — ставим `nginx` (или `caddy`), копируем `dist/` в `/var/www/pod-solncem-site/`, выпускаем Let's Encrypt через `certbot`, настраиваем отдельный server-block для маркетингового поддомена (например, `m.pod-solncem.ru` или нового домена).

### Что нужно от Павла для запуска варианта B

1. **SSH-доступ к серверу** (reg.ru VPS) — пользователь/порт/ключ. **Это отдельная просьба**: в моей SOUL.md `~/.hermes/profiles/raekwon/SOUL.md` Phase 1 — local-only, Phase 2 (remote machines) ещё не активирован.
2. **Решение по домену:** где будет маркетинговый сайт?
   - `m.pod-solncem.ru` (поддомен существующего домена) — но тогда нужно выписать A/CNAME поддомен в зоне `pod-solncem.ru`, что опять требует регистратор-доступ.
   - **Отдельный домен** (как в варианте A) — тогда нужен тот же shortlist + регистратор + DNS.
3. **Certbot + cron** — на VPS уже есть certbot (нужно проверить), либо ставим. Авто-renewal через cron раз в 60 дней.
4. **Решение о HTTP/3 и cache** — Caddy даёт HTTP/3 + авто-HTTPS «из коробки», nginx требует certbot + ручной конфиг + `nginx -s reload`.

### Acceptance criteria для варианта B

- ✅ `https://<chosen-domain>/` → 200 OK, страница отдаётся с VPS (или с поддомена `m.pod-solncem.ru`).
- ✅ HTTP/2 включён, gzip включён, кэш для `/_astro/*` = 1 год (`Cache-Control: public, max-age=31536000, immutable`).
- ✅ Certbot-auto-renew через cron (`certbot renew --quiet`, тест: `certbot renew --dry-run`).
- ✅ Из РФ (Москва, прямой пинг до сервера) — TTFB < 100 мс (если сервер в РФ, напр. Reg.ru в Москве/Cлоне), но **CDN не будет** (это одна точка отказа, не edge).
- ⚠️ **Lighthouse mobile зависит от расстояния.** Если VPS в Москве — будет быстро. Если VPS в US (как у текущего HOSTKEY 82.39.213.82) — будет медленно, Lighthouse mobile может не дотянуть до 90.

### Стоимость

0 ₽/мес (VPS уже оплачен, 9500 ₽ / 3 мес или 16500 ₽ / 6 мес по `CURRENT_STATE.md`). Расход: ~10 минут CPU-time на деплой + 0.1 GB диска.

### Сложность для меня как для Raekwon

- **Средняя–высокая.** Нужен SSH-доступ + Phase 2 (peer через hermes), certbot, nginx/caddy-конфиг, проверка auto-renewal, мониторинг.
- **Время:** 2–3 часа от получения SSH до live-сайта (включая настройку certbot и DNS-пропагацию).

### Минусы (явно из `SITE_ARCHITECTURE.md § 5.3`)

> VPS = одна точка отказа. Сервер уже нагружен (Telegram-бот, Mini App backend).
> Не CDN. Медленнее для пользователей из регионов RU.

Если VPS в US (HOSTKEY 82.39.213.82 — это похоже на правду для текущего сервера) — для РФ-аудитории маркетинговый сайт будет иметь TTFB 200–400 мс, LCP 1.5–3 сек. Lighthouse mobile **< 90, может не сдать**.

### Защита варианта B

Если Pavel принципиально хочет opensource-only (без managed PaaS вообще) — вариант B единственный путь. Если «opensource-friendly / free tier» достаточно — вариант A чище.

---

## Сводная таблица

| Критерий | A (Netlify/CF/Vercel) | B (VPS) |
|---|---|---|
| Цена | 0 ₽/мес | 0 ₽/мес (VPS уже есть) |
| CDN | да (50–250 PoP) | нет |
| Скорость из РФ | excellent | зависит от локации VPS |
| SSL auto | да (hosting) | certbot + cron |
| HTTP/3 | да | да (caddy) или нет (nginx) |
| Lighthouse mobile ≥ 90 | высокая вероятность | зависит от VPS-локации |
| Opensource-only | partial (SaaS-управляемый, но opensource-движок и self-host-возможность) | да |
| Точка отказа | distributed | single (но VPS уже есть) |
| Сложность для Raekwon | низкая (Phase 1, локально) | средняя-высокая (Phase 2, нужен SSH) |
| Phase 1 / Phase 2 | Phase 1 OK | требует Phase 2 активации (peer add) |
| Нужно от Павла | токен managed-PaaS + DNS-доступ | SSH-доступ + DNS-доступ + certbot |

---

## Рекомендация Raekwon

**Вариант A + Cloudflare Pages** — если Pavel готов дать `CLOUDFLARE_API_TOKEN`. CF Pages лучше Netlify для RU-аудитории (PoP в Москве), и это бесплатно без лимитов на bandwidth.

**Вариант A + Netlify** — если у Павла уже есть аккаунт Netlify (тогда даём `NETLIFY_AUTH_TOKEN` от существующего) и он не хочет заводить Cloudflare.

**Вариант B** — только если Павел принципиально хочет self-hosted (есть риск по скорости, если VPS не в РФ).

---

## Что нужно от Павла (минимум одно)

- [ ] Выбрать вариант A (и подвариант CF/Netlify/Vercel) или B.
- [ ] Для A: токен соответствующего PaaS (см. список выше).
- [ ] Для B: SSH-доступ к VPS + разрешение на активацию Phase 2 (peer) — это отдельный процесс, см. `~/.hermes/profiles/raekwon/SOUL.md`.
- [ ] Домен — выбранный из `domains-shortlist.md` + DNS-доступ у регистратора.

Без этих пунктов я НЕ начинаю деплой.