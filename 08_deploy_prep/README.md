# Деплой сайта «Под Солнцем» — README

**Дата начала:** 19.09.2026 (UTC+08).
**Этап:** Э9 — деплой Astro-сайта на production.
**Текущий статус:** **PRE-DEPLOY. Деплой НЕ выполнен. Жду выбора домена и хостинга от Павла.**

---

## Что в этой папке

| Файл | Назначение |
|---|---|
| `README.md` | (этот файл) — общая карта и инструкции |
| `pre-deploy-check.md` | что отдаёт `pod-solncem.ru` сейчас, что лежит в собранном `dist/`, в чём расхождение |
| `domains-shortlist.md` | 5 альтернативных доменов с проверкой доступности и ориентирами цен |
| `deploy-options.md` | 2 варианта деплоя (managed PaaS vs self-hosted VPS), сравнение |
| `dns_records.txt` | шаблоны DNS-записей для каждого варианта |
| `logs/` | логи деплоя (на данный момент пусто — деплой ещё не стартовал) |

---

## TL;DR для Павла

Сайт собран и лежит в `D:\ТУРИЗМ СЕРГЕЙ\07_CODE\site-pod-solncem\dist\` (610 КБ, 16 страниц, sitemap+robots, CTA → Telegram deep-link). На `pod-solncem.ru` уже живёт Telegram Mini App — поэтому деплоим сайт на **отдельный** домен (5 кандидатов в `domains-shortlist.md`), на одном из **2 вариантов** хостинга в `deploy-options.md` (рекомендую Netlify или Cloudflare Pages).

**Ничего не делаю до твоего выбора.** Нужны 3 решения:

1. **Какой домен** берём.
2. **Какой хостинг** (Netlify / Cloudflare Pages / Vercel / VPS).
3. **Токены** для деплоя (`NETLIFY_AUTH_TOKEN`, `CLOUDFLARE_API_TOKEN`, `VERCEL_TOKEN`, или SSH к VPS).

После этого — деплой за 30 минут (PaaS) или 2–3 часа (VPS).

---

## Как обновить сайт (после деплоя)

### Сценарий A: managed PaaS (Netlify/CF Pages/Vercel)
```bash
cd "D:/ТУРИЗМ СЕРГЕЙ/07_CODE/site-pod-solncem"
npm run build             # ~2 сек, → dist/
# PaaS-специфично:
netlify deploy --prod --dir=dist --site=<SITE_ID>
# или
wrangler pages deploy dist --project-name=<PROJECT>
# или
vercel deploy --prod
```

Перед каждым релизом:
```bash
npm run check              # astro check, должен быть 0 errors
git status                 # проверить, что нет незакоммиченных изменений
```

После — проверить в браузере (см. acceptance criteria ниже).

### Сценарий B: self-hosted VPS
```bash
# На локальной машине:
cd "D:/ТУРИЗМ СЕРГЕЙ/07_CODE/site-pod-solncem"
npm run build

# Затем — на сервере (через scp / rsync):
scp -r dist/* root@<VPS_HOST>:/var/www/pod-solncem-site/
ssh root@<VPS_HOST> "nginx -s reload && certbot renew --dry-run"
```

Перед каждым релизом — то же `npm run check`.

---

## Как добавить новую страницу

### Новое направление (`/destinations/<slug>/`)
1. Создать `src/content/destinations/<slug>.mdx` с frontmatter (см. `src/content/config.ts` для схемы).
2. Изображение — `public/images/destinations/<slug>.webp` (WebP, ≤ 200 КБ).
3. `npm run build`. Sitemap обновится автоматически.

### Новый тур (`/tours/<slug>/`)
1. `src/content/tours/<slug>.mdx` с frontmatter (`price`, `duration`, `flightFrom`, `meal`, `badge`, `rating`, `hero`).
2. Картинка — `public/images/tours/<slug>.webp`.
3. `npm run build`.

### Новая страница (политика, новости, контакты)
1. `src/pages/<name>.astro` — минимальный layout + контент.
2. Если это **статичная single-page без коллекции** — можно положить рядом с `index.astro`.
3. `npm run build`.

### Новый CTA-блок (метка для аналитики)
1. В `src/consts/sources.ts` добавить новый label в `BlockSource` union.
2. В `src/components/<ComponentName>.astro` — `<a href={tMeLink('<newLabel>')}>`.
3. Telegram-бот должен понимать новый `start=<newLabel>` (требует правки `07_CODE/telegram-bot/`, **вне зоны Э9** — это задача для Masta Killa / Pavel).

---

## Как откатить (rollback)

### Сценарий A: PaaS
- **Netlify:** Deploys → клик на предыдущий деплой → «Publish deploy».
- **Cloudflare Pages:** в dashboard Pages → Activity → выбрать успешный деплой → «Rollback to this deploy».
- **Vercel:** Deployments → выбрать предыдущий → «Promote to Production».

Все три — UI-операция за 1 клик. Доступ: Pavel (или токен с доступом).

### Сценарий B: VPS
```bash
ssh root@<VPS_HOST>
ls /var/www/pod-solncem-site/               # там лежат версии: v2026-09-19, v2026-09-26, ...
ln -sfn /var/www/pod-solncem-site/v2026-09-19 /var/www/pod-solncem-site/current
nginx -s reload
```
(при условии, что в nginx root указывает на `/var/www/pod-solncem-site/current`.)

### Быстрый откат из командной строки
```bash
# На PaaS: git revert + push, деплой пересоберётся автоматически
cd "D:/ТУРИЗМ СЕРГЕЙ/07_CODE/site-pod-solncem"
git revert HEAD
git push
# → CI/CD пересоберёт
```

---

## Acceptance criteria (полный)

Из задачи `t_4dc744d4`:

- [ ] `https://<chosen-domain>/` — 200 OK, главная сайта (Header + Hero + Trust + Directions + Tours + Manager + Reviews + FAQ + CTA + Footer).
- [ ] `https://<chosen-domain>/sitemap-index.xml` (или `/sitemap.xml`) — 200 OK, реальный XML.
- [ ] `https://<chosen-domain>/robots.txt` — 200 OK, разрешает индексацию.
- [ ] Lighthouse mobile ≥ 90 (через PageSpeed Insights с российским прокси, например 4G RU).
- [ ] DNS-записи — задокументированы в `dns_records.txt` (после выбора хостинга).
- [ ] Лог деплоя — в `09_TESTING_AND_RELEASE/logs/2026-09-deploy.log`.
- [ ] Скриншот главной с production-URL — в `09_TESTING_AND_RELEASE/screenshots/2026-09-deploy/`.
- [ ] Запись в `09_TESTING_AND_RELEASE/EVIDENCE_LOG.md`.
- [ ] Запись в этой папке (`09_DEPLOY/`) — финальный handoff в `02_PROJECT_MANAGEMENT/HANDOFF.md`.

---

## Hard rules (напоминание)

- ❌ НЕ удалять существующий kupit-tyr.ru (если ещё нужен Сергею).
- ❌ НЕ лезть в `07_CODE/frontend-miniapp` и `07_CODE/telegram-bot`.
- ❌ НЕ делать commit/push в основной репо сайта без явного разрешения Павла.
- ❌ НЕ использовать платный SaaS (всё — opensource / free tier / self-hosted).
- ❌ НЕ трогать реквизиты и DNS старого сайта, если они ещё используются.

---

## Связанные задачи / файлы

- `D:\ТУРИЗМ СЕРГЕЙ\03_PRODUCT_AND_ARCHITECTURE\SITE_ARCHITECTURE.md` — основной архитектурный документ (Э1 GZA).
- `D:\ТУРИЗМ СЕРГЕЙ\07_CODE\site-pod-solncem\` — исходники сайта (Astro 5 + Tailwind v4 + MDX + sitemap).
- `D:\ТУРИЗМ СЕРГЕЙ\09_TESTING_AND_RELEASE\EVIDENCE_LOG.md` — журнал доказательств.
- `D:\ТУРИЗМ СЕРГЕЙ\02_PROJECT_MANAGEMENT\HANDOFF.md` — сессионная запись (Э9 здесь будет вписана после деплоя).
- `~/.hermes/profiles/raekwon/SOUL.md` — регламент моей работы (Phase 1 — local-only, Phase 2 — remote через peer).

---

## Контакты / эскалация

- Любые неясности по деплою → RZA → если RZA не может решить, эскалация на Павла через Telegram (`/workspace/spread/`) или через `kanban_comment` на эту задачу.
- Если deploy CLI ломается или выдаёт непонятную ошибку → `kanban_block(reason="...")` и стоп, не угадывать.