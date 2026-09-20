# Pre-deploy проверка: live vs собранный dist

**Дата:** 19.09.2026 20:07 UTC+08.
**Цель:** до деплоя убедиться, что собранный `dist/` отличается от того, что сейчас отдаёт `pod-solncem.ru`, и что не убьём живой Mini App.

---

## Текущее состояние `pod-solncem.ru`

```
$ curl -sI https://pod-solncem.ru/
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Content-Length: 971
Last-Modified: Sun, 16 Aug 2026 18:10:59 GMT

$ curl -s https://pod-solncem.ru/ | head -c 800
<!doctype html>
<html lang="ru">
  <head>
    ...
    <script id="telegram-web-app-sdk" async src="https://telegram.org/js/telegram-web-app.js?63"></script>
    <script type="module" crossorigin src="/as...
```

**Что это:** Telegram Mini App (Vite/React SPA, CSP разрешает `script-src 'self' https://telegram.org`, загружает `assets/index-DCMoFPi1.js`). Задеплоен 16.08.2026, по словам Павла в переписке 09.08.2026 он переносил Mini App сюда из `D:\pod-solncem-miniapp-frontend`.

**IP:** 82.39.213.82 (HOSTKEY, US-локация для сервера, не российский хостер).

## Собранный `dist/` (что у нас в репе)

```
$ du -sh "D:/ТУРИЗМ СЕРГЕЙ/07_CODE/site-pod-solncem/dist/"
610K    D:/ТУРИЗМ СЕРГЕЙ/07_CODE/site-pod-solncem/dist/

$ ls "D:/ТУРИЗМ СЕРГЕЙ/07_CODE/site-pod-solncem/dist/"
_astro/  404.html  agreement/  cookies/  destinations/  favicon.svg  index.html  privacy/  robots.txt  sitemap-0.xml  sitemap-index.xml  tours/
```

**Что это:** Astro 5 + Tailwind v4 static build. 16 страниц (главная + 5 destinations + 4 tours + 3 политики + 404), `sitemap-index.xml` + `sitemap-0.xml`, `robots.txt` — реальные XML/TXT, не SPA catch-all.

## Расхождение

| Аспект | Live pod-solncem.ru | Собранный dist/ |
|---|---|---|
| Тип | SPA (Vite/React) | Static HTML (Astro) |
| Размер index | 971 байт (оболочка) | больше (16 страниц со статикой) |
| Sitemap/robots | SPA catch-all (HTML вместо XML) | реальные XML/TXT |
| CSP | разрешает `https://telegram.org` | без telegram.org в CSP |
| JavaScript | Telegram Web App SDK + React runtime | минимальный остров для cookie-banner |
| Статус | живой Mini App, используется ботом и клиентами | готовая marketing-визитка, **не выкатывалась** |

**Вывод:** если задеплоить `dist/` поверх `pod-solncem.ru` — Mini App перестанет открываться из Telegram, бот потеряет точку входа для новых пользователей, маркетинговый трафик, приходящий на bare-домен, получит «другой» сайт (что может наоборот хорошо — но это Pavel's call).

## Решение (RZA, 18.09.2026)

> По умолчанию выбираем ОТДЕЛЬНЫЙ домен, чтобы не убить живой Mini App на pod-solncem.ru. Mini App живёт, не трогаем.

Это означает: bare `pod-solncem.ru` остаётся за Mini App, маркетинговый сайт деплоится на новый домен из shortlist в `domains-shortlist.md`.

## Что НЕ сделано в этой проверке

- DNS-проверка через `dig/host/nslookup` не прошла из этой машины (DNS 8.8.8.8 timed out, типично для RU VPN/файрвола). Для production-проверки DNS нужен доступ с сервера или из RU-сети.
- WHOIS для `pod-solncem.ru` через nic.ru RDAP вернул 404 (RU-CENTER/TCI RDAP закрыт для публичных запросов, не через партнёров). Регистратор — не подтверждён, нужно уточнить у Павла (см. `domains-shortlist.md`).
- `www.pod-solncem.ru` не проверял (не критично для этого этапа; Mini App использует bare).

## Связанные файлы

- `09_DEPLOY/domains-shortlist.md` — shortlist нового домена.
- `09_DEPLOY/deploy-options.md` — выбор хостинга (вариант A/B).
- `09_DEPLOY/dns_records.txt` — шаблоны DNS-записей под выбранный хостинг.
- `09_DEPLOY/README.md` — общая инструкция деплоя.
- `02_PROJECT_MANAGEMENT/HANDOFF.md` — сессионная запись.
- `09_TESTING_AND_RELEASE/EVIDENCE_LOG.md` — доказательство в журнал.