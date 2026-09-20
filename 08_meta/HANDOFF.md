# Хендофф

Обновляется в конце каждой сессии. Читается в начале следующей.

## Сессия 19.09.2026 (вечер) — ЗАКРЫТИЕ СЕССИИ: ТЗ сайта в PDF + DOC

**Кто:** RZA. **Основание:** USER_DIRECTED Павла 19.09.2026 — «закрывай сессию, подготовь полностью текст всего сайта как техническое задание в формате пдф и док и все на этом».

**Что сделано:**

Собрано полное техническое задание на сайт «Под Солнцем» — единый документ, описывающий весь объём работы с 18 по 19 сентября. ТЗ включает 19 разделов: общие сведения, структура из 16 страниц, дизайн-система (19 цветов, 10 шкал типографики, 29 компонентов), технологический стек (Astro 5 + Tailwind v4), главная (8 блоков с финальными текстами), 5 страниц направлений, 4 страницы туров, 3 страницы-политики, карта Telegram deep-links, SEO-метатеги для 9 страниц, адаптивность и WCAG AA, cookie-баннер, производительность, безопасность, гипотезы требующие подтверждения (раздел 15), ограничения и запреты (раздел 16), приёмка (раздел 17), приложения (структура репо, список задач Kanban, источники).

**Файлы (все в `D:\ТУРИЗМ СЕРГЕЙ\09_TESTING_AND_RELEASE\`):**
- `TZ_POD_SOLNCEM_SITE_v1.0.md` (64 КБ) — исходник Markdown.
- `TZ_POD_SOLNCEM_SITE_v1.0.docx` (38 КБ) — DOCX через `pandoc`. Готов к редактированию в Word/LibreOffice.
- `TZ_POD_SOLNCEM_SITE_v1.0.html` (98 КБ) — промежуточный HTML для предпросмотра в браузере.
- `TZ_POD_SOLNCEM_SITE_v1.0.pdf` (854 КБ) — финальный PDF через `pandoc → HTML → Chrome headless`. Стилизация: PT Serif + Georgia, оранжевый акцент #C8420F, TOC, номера страниц.
- `tz_style.css` (2.7 КБ) — CSS для печати ТЗ.

**Состояние к закрытию:**
- Сайт собран локально в `D:\ТУРИЗМ СЕРГЕЙ\07_CODE\site-pod-solncem\` (16 страниц, `npm run dev/build/preview` зелёные, dist/ 610 КБ, typecheck 0/0/0, скриншоты 320/390/430/1440 в `09_TESTING_AND_RELEASE/screenshots/2026-09-site/`).
- Mini App в `07_CODE\frontend-miniapp` не трогали (HEAD fc50bc5, чисто).
- Telegram-бот в `07_CODE\telegram-bot` не существует, не трогали.
- Деплой **не выполнен** по USER_DIRECTED Павла от 18.09.2026.
- Pre-deploy подготовка Raekwon сделана в предыдущей записи этого файла (см. сессию «19.09.2026 — Э9: pre-deploy подготовка»). 5 доменов проверены, 2 варианта деплоя расписаны, шаблоны DNS-записей готовы. Ждёт решение Павла (домен + хостинг + доступы).

**Что осталось за рамками сессии:**
- Реальное фото менеджера (placeholder в коде).
- Реальные фото направлений и туров (CSS-градиенты).
- Замена 6 шаблонных отзывов на реальные (Сергей не прислал).
- Подтверждение 5 гипотез: контакты, имя менеджера, отзывы, юрлицо, партнёры.
- Git commit и push `07_CODE\site-pod-solncem\` (запрещено без явного разрешения).
- Фактический деплой (заблокирован).

**Следующему исполнителю:**
1. Прочитать `AGENTS.md`, `00_START/CURRENT_STATE.md`, этот файл.
2. Если нужно продолжить по сайту — финальное ТЗ в `09_TESTING_AND_RELEASE/TZ_POD_SOLNCEM_SITE_v1.0.pdf` (или `.docx` / `.md`). Все исходники по ссылкам в ТЗ (приложение В).

**Чего не делать:**
- Не начинать backend, оплату на сайте, Mini App, бота, HeyGen.
- Не менять `04_RESEARCH_AND_DESIGN/00_RAW_CLAUDE_DESIGN`.
- Не объединять репозитории `site-pod-solncem`, `frontend-miniapp`, `telegram-bot`.
- Не делать commit и push без явного разрешения Павла.
- Не считать имя аватара, юрлицо «Под Солнцем» и объём Mini App подтверждёнными.
- Не выдавать гипотезы ТЗ (цены туров, имя «Алина», рейтинги 4.7–4.9, шаблонные отзывы) за подтверждённые данные.

## Сессия 19.09.2026 — Э9: pre-deploy подготовка (деплой НЕ выполнен)

**Кто:** Raekwon. **Основание:** задача `t_4dc744d4` (Э9 деплой). **Зависимости:** Э6 (Masta Killa, 18.09 — `t_3b5aba08` done, dist/ собран, 16 страниц, 610 КБ).

**Контекст:** на `pod-solncem.ru` уже живёт Telegram Mini App (Vite/React SPA, задеплоен 16.08.2026 из `D:\pod-solncem-miniapp-frontend`, IP 82.39.213.82 HOSTKEY US). Задеплоить поверх него Astro-маркетинг = убить Mini App. По разъяснению RZA от 18.09.2026: «выбираем ОТДЕЛЬНЫЙ домен, Mini App не трогаем. Имя ИИ-аватара НЕ ВПИСЫВАТЬ. Mini App НЕ ТРОГАТЬ. До выбора Павла НИЧЕГО НЕ ДЕПЛОИТЬ».

**Что сделано (pre-deploy, без деплоя):**

- `D:\ТУРИЗМ СЕРГЕЙ\09_DEPLOY\` (создана папка, 5 файлов):
  - `README.md` (8.7 КБ) — общая карта: что в папке, TL;DR для Павла, как обновить/добавить страницу/откатить, acceptance criteria, hard rules, эскалация.
  - `pre-deploy-check.md` (4.7 КБ) — фиксация расхождения live vs dist/ + решение RZA.
  - `domains-shortlist.md` (5.5 КБ) — 5 альтернативных доменов с проверкой доступности через RDAP.org:
    - `pod-solncem.store` ✅ «is available for registration» (radix.host, явное подтверждение).
    - `pod-solncem.online` ✅ «is available for registration».
    - `pod-solncem.site` ✅ «is available for registration».
    - `pod-solncem.travel` ✅ 404 «Object not found» через Identity Digital (сильный сигнал свободен).
    - `pod-solncem.tours` ✅ 404 «Object not found» через Identity Digital (сильный сигнал свободен).
    - `ps-travel.ru` / `podsolncem.ru` / `pod-solncem-website.ru` — .ru RDAP закрыт публично, нужна проверка из reg.ru-кабинета Павла.
  - `deploy-options.md` (12.2 КБ) — два варианта деплоя (A: managed PaaS, рекомендую Netlify или Cloudflare Pages; B: self-hosted VPS, требует Phase 2). Сводная таблица, стоимость, сложность, acceptance.
  - `dns_records.txt` (6.2 КБ) — шаблоны DNS-записей для 4 хостеров (Netlify / CF Pages / Vercel / VPS) + редирект www↔bare + чек-лист после прописи.
- `D:\ТУРИЗМ СЕРГЕЙ\09_TESTING_AND_RELEASE\logs\2026-09-deploy.log` (5.6 КБ) — лог pre-deploy prep (8 пунктов с командами, exit code, выводами).
- `D:\ТУРИЗМ СЕРГЕЙ\09_TESTING_AND_RELEASE\EVIDENCE_LOG.md` — добавлено 6 строк (Э9 pre-deploy inventory, dist readiness, domain availability, CLI inventory, pre-deploy artifacts, deploy pending).

**Что НЕ сделано (явно, по запросу RZA):**

- Не задеплоен `dist/` никуда.
- Не зарегистрирован новый домен (нужны токены/оплата от Павла).
- Не прописаны DNS-записи.
- Не выдан TLS-сертификат.
- `pod-solncem.ru` НЕ тронут, Mini App НЕ тронут.
- `07_CODE/frontend-miniapp` и `07_CODE/telegram-bot` НЕ тронуты.
- Коммитов и push в `07_CODE/site-pod-solncem/` НЕ делал (Phase 1, деплой через CLI после выбора хостинга).

**Нужны от Павла 3 решения (см. `09_DEPLOY/README.md` § TL;DR):**

1. Домен — из shortlist (рекомендую `pod-solncem.travel`, бренд + тематическая зона) или свой.
2. Хостинг — вариант A (Netlify / CF Pages / Vercel, рекомендую CF Pages для RU-аудитории) или вариант B (VPS).
3. Доступы — `NETLIFY_AUTH_TOKEN` / `CLOUDFLARE_API_TOKEN` / `VERCEL_TOKEN` для A; SSH-ключ для B. Плюс доступ к DNS-зоне у регистратора.

После получения — деплой за 30 мин (PaaS) или 2–3 ч (VPS). Acceptance criteria (см. `09_DEPLOY/README.md` § acceptance): live URL 200 OK, sitemap 200 OK, robots 200 OK, Lighthouse mobile ≥ 90 из РФ, скриншот в `09_TESTING_AND_RELEASE/screenshots/2026-09-deploy/`, запись в EVIDENCE_LOG.

**Состояние Git:** `07_CODE/site-pod-solncem/` без изменений (Phase 1, dist/ не пересобирал, коммитов не делал). Mini App repo HEAD не менял. Чисто.

**Следующий шаг:** ждать выбора Павла → после получения токенов/SSH повторно открыть `t_4dc744d4` (или новую задачу от RZA) и выполнить фактический деплой + скриншоты + финальный EVIDENCE_LOG.

## Сессия 18.09.2026 (ночь) — Э3: дизайн-система и mobile-first макеты сайта

**Кто:** U-GOD. **Основание:** задача `t_64dae841` (Э3). Зависимости: Э0 (RZA, SITE_SCOPE.md) и Э1 (GZA, SITE_ARCHITECTURE.md) — оба done. Mini App и Telegram-бот НЕ трогались.

**Что сделано:**
- Палитра снята пипеткой с `D:\ТУРИЗМ СЕРГЕЙ\04_RESEARCH_AND_DESIGN\01_SITE_DESIGN\REFERENCE.png` (`dev/extract_palette.py`). Приведена к WCAG AA: кнопочный accent затемнён до `#C8420F` (reference orange `#F2601B` даёт 3.25:1 с белым — не проходит AA-normal). Точная референсная сохранена как `accentBright` для декоративных бейджей и лучей солнца.
- `D:\ТУРИЗМ СЕРГЕЙ\04_RESEARCH_AND_DESIGN\01_SITE_DESIGN\DESIGN.md` (40 КБ, lint: **0 errors, 5 warnings** — все decorative/orphaned, не блокирующие). Содержит: colors (19 hex), typography (10 scales: PT Serif для заголовков и цен, Onest для UI и тела, Caveat для рукописных подписей), spacing 4pt grid, breakpoints 320/390/430/768/1024/1280/1440, rounded scale, motion, components (29 entries: button×3, card×5, badge×7, input×3, accordion×2, header-bg, footer-bg, text-muted×2, badge-info), states (default/hover/active/focus-visible/disabled), иконография (inline SVG only).
- Экспорты в `D:\ТУРИЗМ СЕРГЕЙ\04_RESEARCH_AND_DESIGN\01_SITE_DESIGN\exports\`:
  - `tokens.json` — W3C DTCG (438 строк)
  - `theme.css` — Tailwind v4 `@theme` block (70 строк, готов к подключению в `src/styles/global.css`)
  - `tailwind.theme.json` — Tailwind v3 compat
  - В рабочем пространстве задачи (`workspace/exports/`): `tokens.ts` для Astro (`src/consts/tokens.ts`), `global.css` (стартовый, 11 КБ, содержит :root, @theme, btn-primary/secondary/card/badge/input утилиты), `tokens.dtcg.json`, `theme.tailwind-v4.css`, `tailwind.theme.json`.
- Логотип-солнце отрисован вручную как inline SVG: `dev/logo-sun.svg` (320×80, full lockup «ПОД СОЛНЦЕМ + ТУРИСТИЧЕСКОЕ АГЕНТСТВО»), `dev/logo-mark.svg` (80×80, только маркер). 8 лучей + полукруг + 2 волны. Цвета `logoSun #F89028` + `accentBright #F2601B`.
- Mobile-first HTML-мокап главной: `dev/home.html` (51 КБ). Все 8 блоков SCOPE + финальный CTA-баннер. Реальный контент: Турция/ОАЭ/Таиланд/Грузия, цены 89/145/198/58 тыс ₽ на двоих, 4 типа бейджей (Хит продаж/Популярно/Выбор туристов/Низкая цена), менеджер Алина, 4 отзыва с именами и городами, 4 пункта «Почему нам доверяют», 7 вопросов FAQ. Все CTA → `https://t.me/pod_solncem_travel_bot?start=<source>` (метки: header/hero/manager/tour_tr/tour_uae/tour_th/tour_ge/banner).
- Скриншоты в `workspace/mockups/`: `320.png` (320×9313), `390.png` (390×9426), `430.png` (430×9605), `full.png` (1440×4911), `above-fold.png` (1440×900). Проверено: scrollWidth === clientWidth на всех ширинах (320/390/430/1440) — горизонтального скролла нет.
- Компонентные мокапы `workspace/components/`: `header.png`, `cards-tour.png` (все 4 варианта бейджа в ряд), `card-direction.png` (5 в ряд), `card-review.png`, `block-manager.png` (фото + цитата + 3 буллита + CTA + подпись «Буду рада помочь!»), `block-faq.png` (закрытый + открытый), `block-footer.png` (лого + меню + контакты + подписка), `buttons.png` (primary/disabled/secondary/outline).
- Блок-карта: `workspace/block-map.png` — аннотированный макет с пронумерованными блоками 1–10 (Header → Hero → Trust → Directions → Tours → Manager → Reviews → Why us + FAQ → CTA → Footer) + легенда вверху с пояснением каждого.
- WCAG AA проверен (`dev/wcag_check.py`): все ключевые текстовые пары (text-primary на surface 16.31, text-on-accent на accent 4.95, text-secondary на surface 6.92, muted на surface 5.48) проходят AA-normal. Reference `#F2601B` на белом (3.25) помечен как decorative-only.

**Что НЕ сделано / ждёт ответов Сергея (см. `OPEN_QUESTIONS_TO_SERGEY.md`):**
- Реальный телефон / email / адрес офиса — везде заглушка `+7 (495) 123-45-67` / `info@pod-solncem.ru` / «г. Москва, ул. Путешественников, д. 1».
- Фото менеджера — placeholder (нейтральная иллюстрация, SVG-круг + эллипс).
- Имя «Алина» — гипотеза; помечено в SCOPE как требующее подтверждения.
- Точные цены туров — гипотетические.
- ID Яндекс.Метрики — ставим с placeholder; cookie-баннер готов.

**Состояние Git:** frontend main HEAD `fc50bc5`, status чистый. Эта сессия НЕ правила код. Все артефакты — в `04_RESEARCH_AND_DESIGN/01_SITE_DESIGN/` и в workspace `t_64dae841`. Манифесты для Masta Killa (Э6) готовы: tokens.ts, global.css, DESIGN.md, mockups/, components/, block-map.png.

**Следующий шаг:** Э6 (Masta Killa) поднимает Astro-проект по `SITE_ARCHITECTURE.md`, используя токены из `tokens.ts` + `global.css`. Мокапы передаются как референс для имплементации компонентов. Inspectah Deck (QA) сверяет контрасты и mobile-fit на готовой сборке.

## Сессия 18.09.2026 — сбор и анализ канала @coral_taganskaya

**Кто:** Cline. **Основание:** прямой запрос Павла: изучить Telegram-канал агентства, собрать сырьё в папку «СЫРЬЁ ДЛЯ НОВОГО САЙТА» и провести анализ для нового сайта.

- Создана `D:\ТУРИЗМ СЕРГЕЙ\СЫРЬЁ ДЛЯ НОВОГО САЙТА\СЫРЬЁ С КАНАЛА`: posts.json на 3 433 записи (экспорт Telegram 3 386 сообщений 2023-09-22…2026-08-25 + 47 постов веб-ленты 15–16.09.2026, ID 5212–5443), реестр медиа-ссылок 4 243 записи (сами фото/видео в экспорт не включены и не скачаны), 5 CSV-датасетов, summary.json, HTML-обзор `ОБЗОР_КАНАЛА.html`, README с границами и планом.
- Анализ (кандидаты, не факты): 983 поста с ценой, 2 960 со ссылками kupit-tyr.ru, 1 191 с CTA, 1 375 с реакциями, 961 отель, 83 поста-совета, 220 хэштегов; топ-направления: Турция 331, Египет 250, ОАЭ 195, Таиланд 173, Вьетнам 140, Россия 88, Мальдивы 84.
- Проверки: `verify_merge.py` PASS (все экспортные сообщения на месте, тексты/даты идентичны, первые 100 сверены с контрольным CSV), `validate_outputs.py` ALL PASS (30 проверок: схемы CSV, пересчёт тегов/стран/цен из posts.json, целостность HTML, реестр медиа). Сквозной прогон пяти скриптов: OVERALL PASS, лог `D:\ТУРИЗМ СЕРГЕЙ\09_TESTING_AND_RELEASE\logs\2026-09-18_channel_collection_e2e.log` (копия в `05_ПРОВЕРКИ\end_to_end.log`).
- Не сделано: скачивание фото/видео (в экспорте пометки «File not included», права не подтверждены), полный ре-экспорт канала (нужен доступ Сергея), проверка контактов из постов. Цены из постов признаны непубликуемыми.
- Состояние Git: frontend main, HEAD fc50bc578bfe43e04b220c228862133631e82f52, status чистый; код не менялся, commit/push не выполнялись, разрешение не запрашивалось. FEATURE_LIST не менялся: сбор источников по прямой задаче, не функция.
- Следующий шаг: показать Сергею ОБЗОР_КАНАЛА.html, отобрать направления/отели/советы, получить медиа-оригиналы и подтверждение контактов.

## Сессия 17–18.09.2026 — архив сайта kupit-tyr.ru

**Кто:** Cline. **Основание:** прямой запрос Павла собрать сырьё сайта клиента в отдельную папку. Эта запись новее описанной ниже августовской сессии; прежний handoff сохранён.

- Создана `D:\ТУРИЗМ СЕРГЕЙ\СЫРЬЁ ДЛЯ НОВОГО САЙТА`: 88 HTML основного сайта и тексты, 6 связанных страниц (из них Невылет.рф — сторонний сервис), 5 публичных Telegram-страниц, единый Markdown, CSV/JSON реестры, 69 локальных файлов медиа, две аналитические сводки, README, проверка и SHA-256-манифест.
- Проверка: `python "D:\ТУРИЗМ СЕРГЕЙ\СЫРЬЁ ДЛЯ НОВОГО САЙТА\04_ТЕХНИКА\verify_archive.py"` — PASS для 99 HTML/Markdown, 88 основных страниц в общем тексте, файловых ссылок отчётов и сигнатур/непустоты 69 медиа.
- Архив **частичный**, не полный офлайн-сайт: 178 подходящих локальных ресурсов не загружались, 1 ресурс вернул 404. В итоговом списке 20 несохранённых внутренних URL (9 проверенных 404, остальные не запрошены), плюс недоступный поддомен hotels. Один медиафайл не имеет записи в финальном сетевом реестре; путь зафиксирован.
- Не сделано: браузерная проверка, скриншоты, живые цены/выдача виджетов, полный Telegram, внешние медиа, CMS-бэкап и разработка нового сайта. Заявки и платежи не отправлялись. Юрлицо/партнёры/реквизиты/офисы сохранены как утверждения старого сайта, а не клиентские подтверждения.
- Фактический Git при первой выполненной проверке и в конце: frontend `main`, HEAD `fc50bc578bfe43e04b220c228862133631e82f52`, status чистый. Проверка Git была выполнена после начала сбора, не до него. Код репозиториев не менялся. Commit/push не делались, разрешения не было.
- Статусы FEATURE_LIST не менялись: это сбор источников по прямой задаче, не реализация функции Mini App.
- Доказательство: `D:\ТУРИЗМ СЕРГЕЙ\09_TESTING_AND_RELEASE\logs\2026-09-18_site_archive_verification.log`; оригинал — `D:\ТУРИЗМ СЕРГЕЙ\СЫРЬЁ ДЛЯ НОВОГО САЙТА\04_ТЕХНИКА\final_verification.log`.
- Следующий шаг: пройти с Сергеем сводки и отметить, какие контакты/офисы/услуги/документы переносить, обновлять или исключать.

## Сессия 18.09.2026 (вечер) — запуск задачи «новый сайт с нуля»

**Кто:** RZA. **Основание:** USER_DIRECTED Павла 18.09.2026 — «делаем сайт с нуля по референс-картинке», Mini App и Telegram-бот НЕ трогаем. Палитра зафиксирована по референсу, форма продающая, визуал позже через Claude Design.

- `D:\ТУРИЗМ СЕРГЕЙ\03_PRODUCT_AND_ARCHITECTURE\SITE_SCOPE.md` (14.3 КБ) — 8 блоков главной по референсу + 5 страниц направлений + 4 страницы туров + 3 страницы-политики. Палитра зафиксирована. Принцип продающей подачи в разделе 3 SCOPE.
- `D:\ТУРИЗМ СЕРГЕЙ\01_CLIENT_AND_SCOPE\OPEN_QUESTIONS_TO_SERGEY.md` (9.6 КБ) — 5 вопросов (контакты/офисы, менеджер Алина, отзывы, юрлицо, партнёры). По каждому дефолт.
- Референс-картинка в `D:\ТУРИЗМ СЕРГЕЙ\04_RESEARCH_AND_DESIGN\01_SITE_DESIGN\REFERENCE.png`.
- В Kanban 7 задач: `t_229ffdd0` Э0 RZA (ready), `t_644bd56d` Э1 GZA (gated Э0), `t_76d3e5cd` Э2 Copywriter (gated Э0), `t_1b3f488b` Э5 GZA (gated Э0), `t_90a0ddd4` Э7 Ghostface (gated Э0), `t_e58b2ff9` Э8 Ghostface (gated Э2), `t_64dae841` Э3 U-GOD (gated Э0+Э1).
- Git не менялся, frontend main HEAD fc50bc5, status чистый. Код Mini App не трогали.
- Следующий шаг: закрыть Э0 → разблокируются остальные 6 → Masta Killa (Э6 сборка) появится после Э2+Э3, Raekwon (Э9 деплой) после Э6, RZA (Э10 проверки + Э11 handoff) последними.

## Сессия 18.09.2026 (ночь) — Э1: выбор стека и архитектура

**Кто:** GZA. **Основание:** задача `t_644bd56d` (Э1). Дополнение от RZA-комментария: палитра ЗАФИКСИРОВАНА, формы = ОБЯЗАТЕЛЬНО telegram deep-link, 5 направлений + 4 тура + политики, mobile-first, opensource/self-hosted где возможно.

- `D:\ТУРИЗМ СЕРГЕЙ\03_PRODUCT_AND_ARCHITECTURE\SITE_ARCHITECTURE.md` (29.6 КБ, 374 строки). Выбран стек: **Astro 5 (static output) + Tailwind v4 + @astrojs/mdx + @astrojs/sitemap**. Деплой: Netlify (основной), Vercel/Cloudflare Pages (запасные), VPS НЕ рекомендован. GitHub Pages НЕ рекомендован (нет PR preview).
- Обоснование (3 абзаца): НЕ Next.js (90–130 КБ React runtime per route — лишний вес для 20 статичных страниц), НЕ чистый Vite (нет Content Collections / MDX / sitemap — придётся писать руками). Astro — «HTML по умолчанию» + контент-слой. Источники: Vercel `astro-vs-next-js`, LogRocket `astro-vs-next-js-ssg-vs-react`, Prerendering `nextjs-vs-remix-vs-astro-for-seo` (апр 2026), Tailwind docs по Astro, Telegram docs по `?start=<payload>` (GramIO guide).
- Структура папок до 2 уровней: `src/{layouts,components,pages,content,lib,consts,styles}` + `public/{images,fonts}` + `scripts/`. Контент-файлы для Copywriter: `src/content/{destinations,tours,reviews,faq}/*.mdx`.
- Как формы становятся Telegram deep-link'ами: одна функция `tMeLink(source)` возвращает `https://t.me/pod_solncem_travel_bot?start=<source>`, где source — типобезопасный enum из 12 меток (`hero|manager|callback|newsletter|dest_*|tour_*`). Ноль POST, ноль backend. Email-подписка на влог → вариант A (через бот, `/start newsletter`).
- Как деплоится на pod-solncem.ru: Netlify free tier, `netlify.toml` с заголовками кэша, DNS — CNAME `www` + A `@` (после добавления домена Netlify выдаёт). HTTPS авто.
- 5 открытых уточнений для Сергея/Павла — НЕ блокируют архитектуру (это контент-поля, не структурные). Зафиксированы в § 8 архитектуры.
- Дочерние задачи Э1 (на разблокировке после Э1→done): `t_64dae841` Э3 U-GOD. Э2/Э5/Э7/Э8 разблокируются после Э0 (RZA), не от Э1.
- Git не менялся, frontend main HEAD fc50bc5, status чистый. Эта сессия НЕ правила код.
- Следующий шаг: U-GOD подбирает палитру по REFERENCE.png, Masta Killa (Э6) появляется только после Э2+Э3 и поднимает Astro-проект по `SITE_ARCHITECTURE.md`.

## Сессия 18.09.2026 (ночь) — Э7: юридические тексты для сайта

**Кто:** Ghostface. **Основание:** задача `t_90a0ddd4` (Э7). Согласовано с Павлом: адаптировать существующий пакет документов для бота под новый сайт `pod-solncem.ru`.

**Что сделано:**
- `D:\ТУРИЗМ СЕРГЕЙ\01_CLIENT_AND_SCOPE\SITE_LEGAL\01_privacy_policy.md` (22.8 КБ, 196 строк). Политика обработки ПДн по 152-ФЗ. Явно описан маршрут данных формы: Сайт → Telegram-бот `@pod_solncem_travel_bot` через deep-link. **Email и собственный сервер в маршруте не участвуют.**
- `D:\ТУРИЗМ СЕРГЕЙ\01_CLIENT_AND_SCOPE\SITE_LEGAL\02_cookie_consent.md` (6.8 КБ, 79 строк). Cookie-уведомление + текст баннера. Технические cookie (обязательные) + аналитические cookie Яндекс.Метрики (только после согласия). Две кнопки: «Принять» и «Только необходимые».
- `D:\ТУРИЗМ СЕРГЕЙ\01_CLIENT_AND_SCOPE\SITE_LEGAL\03_user_agreement.md` (13.7 КБ, 123 строки). Пользовательское соглашение. Явно НЕ оферта на продажу тура; оферта на договор о реализации туристского продукта заключается отдельно.
- `D:\ТУРИЗМ СЕРГЕЙ\01_CLIENT_AND_SCOPE\SITE_LEGAL\README.md` (10.7 КБ, 91 строка). Что готово, что ждёт подтверждения Сергея, что нужно от U-GOD, чек-лист перед публикацией.

**Что НЕ использовано из старого пакета (намеренно):**
- «ООО «Под Солнцем»» как подтверждённое юрлицо — Сергеем письменно не подтверждено. В текстах: «турагентство «Под Солнцем» (ИП/самозанятый, реквизиты уточняются)».
- Бренды Coral Travel, Coral Elite Service — Сергей «уходит от франшизы» (голосовое 18.09), подтверждения не было.
- Имя ИИ-аватара (Анна/Анастасия) — не вписано.
- Email `coralclub5av@mail.ru` — относится к старому ООО. Заменён на `info@pod-solncem.ru` (дефолт вопроса 1.4 OPEN_QUESTIONS_TO_SERGEY).
- Реальные номера телефонов `+7 (495) 212-14-21`, `+7 (906) 713-73-37`, `+7 (967) 117-11-88` — относятся к старому ООО. Заменены на заглушку `+7 495 ***5127` (по условию задачи).
- Банковские реквизиты — НЕ публикуются (только в договорах).
- Адрес офиса — не конкретизирован, оставлен «уточняется».

**Состояние Git:** Эта сессия не трогала код. Git в `07_CODE/frontend-miniapp` не менялся. Все артефакты — только в `01_CLIENT_AND_SCOPE\SITE_LEGAL\`.

**Что НЕ сделано и почему:**
- Не конкретизирован Оператор (юрлицо, ИНН, юрадрес, реальный телефон, реальный email) — ждём ответов Сергея по вопросам 1.1–1.4, 4.1 OPEN_QUESTIONS_TO_SERGEY.md.
- Не подтверждено включение Яндекс.Метрики — дефолт «ставим», но ID от Сергея не получен. Cookie-уведомление подготовлено в расчёте на включение Метрики; если Сергей откажется, раздел 2.2 нужно вырезать.
- Не включено согласие на email-рассылку (Приложение № 1 к старой политике) — на текущем Сайте email Пользователя не запрашивается, форма не содержит чекбокса рассылки. Если в v2 появится подписка на влог — добавить отдельным документом.

**Доказательства:** grep-проверка запрещённых токенов в публичных текстах — ноль совпадений по «ООО», «Вихров», «Coral», «Анна», «Анастасия», «coralclub5av», ИНН/ОГРН, реальным номерам телефонов. Все эти токены встречаются только в README.md в разделе «что НЕ использовано и почему».

**Следующий шаг:** Э8 (Ghostface, `t_e58b2ff9`) — тексты для страниц направлений и туров, gated от Э2 (Copywriter). Эта задача готова к публикации сразу после ответа Сергея по 5 открытым вопросам из `OPEN_QUESTIONS_TO_SERGEY.md`.

## Последняя сессия
**Дата:** 11.08.2026
**Кто работал:** Mavis (Mavis Code), затем Ghostface (правка)
**Что делали:** собрать каталог отелей по 7 странам для базы знаний ИИ-аватара и Telegram-бота по прямой задаче Павла. Страны: Турция, Вьетнам, Мальдивы, ОАЭ, Египет, Таиланд, Китай. Затем — собрать из брифа и шаблона один .docx-пакет документов для бота (Условия использования + Политика ПДн + Согласие на рассылку).
## Что сделано в сессии 11.08.2026

- В чате `01_CLIENT_AND_SCOPE/RAW_SOURCES/telegram-export-23-07_09-08-2026.json` найдены и зафиксированы: точная цитата Сергея со списком стран (id 526418), две рекламы отелей из дайджеста kupit-tyr.ru (id 6292490273 и 6292503245), GEO-стратегия Сергея (id 526715), которая задаёт формат описания тура.
- Создана папка `05_CONTENT/07_HOTEL_CATALOG/`.
- В этой папке два файла:
  - `README.md` — методология, источники, статусы, формат карточки, что добавить дальше.
  - `hotels-by-country.md` — каталог на 35 отелей: 5 на каждую из 7 стран, единый шаблон описания (страна, курорт, питание, пляж, для кого, плюсы, минусы, фишка, рейтинги пляжа/питания/сервиса, источник проверки, статус).
- Из 35 отелей 2 имеют статус «✅ подтверждён kupit-tyr.ru» (Aurora Oriental Resort в Египте, Hampton By Hilton Marjan Island в ОАЭ). 33 имеют статус «🆗 требует подтверждения менеджером», это гипотеза из публичных источников, помечены явно.
- Этот файл `HANDOFF.md` обновлён.
- Собран и проверен пакет документов для бота: `01_CLIENT_AND_SCOPE/gen_pdn/Документы_для_бота_Под_Солнцем.docx` (22 036 байт, 23 файла внутри, 300 строк текста). Три раздела в одном файле: Условия использования, Политика обработки персональных данных (152-ФЗ), Согласие на новостную и рекламную рассылку. 26/26 контент-проверок OK. Запись в `09_TESTING_AND_RELEASE/EVIDENCE_LOG.md`, лог в `09_TESTING_AND_RELEASE/logs/2026-08-11_docx_pack_check.log`. Имя ИИ-аватара не внесено, банковские реквизиты не вынесены в публичный документ, замаскированный телефон +7 495 ***5127 не включён.

## Что не сделано и почему

| Что | Почему |
|---|---|
| Commit и push | запрещено без явного разрешения Павла |
| Круизный каталог | не входило в задачу этой сессии, вынесено в следующий шаг |
| Фотографии направлений Вьетнам/Мальдивы/Таиланд/Китай | не входило в задачу, нужно дождаться материалов от Сергея |
| Сверка каталога с реальным списком стран в Mini App | Паша обещал прислать скрины Mini App, на момент создания каталога скрины не пришли |
| Подтверждение 33 отелей Сергеем | нельзя сделать без живого общения, передаётся Сергею через Павла |
| Сайт kupit-tyr.ru | возвращает 502 Bad Gateway, прямой парсинг каталога невозможен |
| Подтверждение у Сергея двух договоров (турист + агентский с туроператором) | запрошено в брифе, не получено — без подтверждения договоры в пакет не входили |
| Проверка .docx пакета в MS Word / LibreOffice | локально недоступно (нет soffice/Word), валидность подтверждена ZIP-целостностью и auto-extract текста; визуальная проверка — за Павлом |

## Состояние на конец сессии

| Что | Значение |
|---|---|
| Рабочее пространство | `D:\ТУРИЗМ СЕРГЕЙ`, готово |
| HEAD frontend | fc50bc5, чисто, CRLF-шум не считается изменениями |
| Активный этап | P01 |
| Критичных блокеров | 4 |
| Открытых вопросов | 20 |

## Состояние артефактов сессии 11.08.2026 (дополнение Ghostface)

| Артефакт | Путь | Размер | Статус |
|---|---|---|---|
| Пакет документов для бота | `01_CLIENT_AND_SCOPE/gen_pdn/Документы_для_бота_Под_Солнцем.docx` | 22 036 байт | собран, 26/26 проверок OK |
| Лог проверки | `09_TESTING_AND_RELEASE/logs/2026-08-11_docx_pack_check.log` | 1 961 байт | записан |
| Запись в EVIDENCE_LOG | `09_TESTING_AND_RELEASE/EVIDENCE_LOG.md` | — | добавлена |

## Следующему исполнителю

1. Прочитать `AGENTS.md`.
2. Прочитать `00_START/CURRENT_STATE.md`.
3. Прочитать этот файл.
4. Проверить Git в `07_CODE/frontend-miniapp`.
5. Выполнить единственный следующий шаг из `00_START/NEXT_ACTION.md`.
6. Не повторять сделанное: систематизация, IA, User Flow, wireframes и frontend уже готовы.

## Чего не делать

- Не начинать backend, бота, HeyGen до этапа P02.
- Не менять `04_RESEARCH_AND_DESIGN/00_RAW_CLAUDE_DESIGN`.
- Не объединять frontend и Telegram-бот в один репозиторий.
- Не выполнять commit и push без явного разрешения Павла.
- Не считать имя аватара, юрлицо «Под Солнцем» и объём Mini App подтверждёнными.

## Шаблон следующей записи

```text
Дата:
Кто работал:
Что сделано:
Что не сделано и почему:
Состояние Git (HEAD, ветка, status):
Какие функции перешли в статус implemented или verified:
Какие доказательства записаны в EVIDENCE_LOG:
Следующий шаг (один):
```

---

## Запись 18.09.2026 — Э6 (Masta Killa): сборка сайта «Под Солнцем»

**Дата:** 18.09.2026 (UTC+08).
**Кто работал:** Masta Killa.
**Сессия:** `kanban t_3b5aba08` — карточка «[Э6-retry] Сборка сайта „Под Солнцем“ на Astro (clean)».

**Что сделано:**
- Создан новый репозиторий `D:\ТУРИЗМ СЕРГЕЙ\07_CODE\site-pod-solncem\` (НЕ в `07_CODE\frontend-miniapp` и НЕ в `07_CODE\telegram-bot`).
- Инициализирован Astro 5 проект:
  - `package.json`: astro@5, @astrojs/mdx, @astrojs/sitemap, @astrojs/check, tailwindcss@4, @tailwindcss/vite, typescript.
  - `astro.config.mjs`: output:'static', site:'https://pod-solncem.ru', trailingSlash:'never', integrations: [mdx(), sitemap()], vite: [tailwindcss()].
  - `tsconfig.json`: extends astro/tsconfigs/strict.
  - `src/styles/global.css`: `@import "tailwindcss"` + `@theme` блок с палитрой, шрифтами, type-scale, radii, spacing (синхронизировано с `04_RESEARCH_AND_DESIGN/01_SITE_DESIGN/exports/theme.css`).
  - `src/env.d.ts`: тип для `import.meta.env.PUBLIC_*`.
- Утилиты (TypeScript):
  - `src/consts/tokens.ts` — TS-копия дизайн-токенов (`colors`, `radii`, `spacing`).
  - `src/consts/sources.ts` — `SOURCES` enum из 17 меток: hero, directions, tours, manager, callback, newsletter, `dest_{slug}` × 5, `tour_{tr|ae|th|ge}` × 4. Тип `BlockSource` выводится автоматически.
  - `src/consts/site.ts` — `SITE_PHONE_DISPLAY`, `SITE_PHONE_HOURS`, `SITE_EMAIL`, `SITE_ADDRESS_FULL`, `LEGAL_FORM`, `SITE_URL`, `SITE_BRAND`. Все гипотетические значения помечены `// TODO(sergey)`.
  - `src/consts/seo.ts` — meta title/description/h1/path/keywords для главной, 5 направлений, 4 туров, 3 политик. Все title ≤60 chars и description ≤160 chars проверено.
  - `src/lib/telegram.ts` — `tMeLink(source: BlockSource)` читает `PUBLIC_TELEGRAM_BOT_USERNAME` из env, возвращает `https://t.me/<bot>?start=<source>`. Одна функция — никто руками URL не пишет.
  - `src/lib/seo.ts` — `renderSeoTags(seo)` генерирует `<title>`, `description`, `robots`, `canonical`, `og:*`, `twitter:*` из `PageSeo`.
  - `src/lib/icons.ts` — 25+ inline SVG иконок (24×24 viewBox, stroke 1.5px, currentColor). `IconName` тип.
  - `src/lib/content.ts` — типизированные массивы `DESTINATIONS` (5), `TOURS` (4), `REVIEWS` (6), `FAQS` (7), `TRUST_POINTS` (4), `TRUST_BADGES` (3). Замена MDX-коллекций — все данные для страниц в одном TS-модуле с типами. Каждое числовое значение помечено гипотезой.
- Layouts:
  - `src/layouts/BaseLayout.astro` — `<html>`, head (Google Fonts, SEO, Yandex.Метрика скриптом при consent), Header, slot, Footer, CookieBanner. Yandex.Метрика инжектится ТОЛЬКО если `localStorage.ps_cookie_consent === 'accepted'`. Иначе — no-op.
  - `src/layouts/ContentLayout.astro` — для страниц направлений/туров: узкий hero + CTA + контент.
- Компоненты (`src/components/`):
  - `Logo.astro` — солнце + 8 лучей + 2 волны + «ПОД СОЛНЦЕМ» + «туристическое агентство». Inline SVG. `variant: 'color' | 'mono'` (для тёмного футера).
  - `Header.astro` — sticky logo + nav + телефон + CTA + mobile drawer (`<480px` бургер, `768px+` всегда виден). Скролл-тень после 100px.
  - `Hero.astro` — eyebrow + H1 + subtitle + primary CTA «Подобрать отдых за 60 секунд» + secondary outline CTA + photo placeholder с подписью Caveat «Мир ближе, чем кажется». Mobile: photo вверху; desktop: photo справа.
  - `TrustBadges.astro` — 3 бейджа в одну строку на desktop.
  - `DestinationsGrid.astro` — 5 карточек (1/2/5 колонок на мобиле/планшете/десктопе).
  - `ToursCarousel.astro` — 4 тура с бейджами (4 типа цветов), рейтингом, вылетом, питанием, ценой, CTA «Посмотреть тур →» на каждой карточке.
  - `ManagerBlock.astro` — фото (плейсхолдер «А» в кружке) + имя «Алина» (помечено «гипотеза, требует подтверждения») + цитата + 3 буллита + подпись Caveat «Буду рада помочь!» + primary CTA.
  - `Reviews.astro` — 6 отзывов с маркером «образец». 1/2/4 колонки.
  - `WhyUs.astro` — 4 пункта с большим бледным номером на фоне.
  - `Faq.astro` — 7 раскрывающихся вопросов нативным `<details>/<summary>`, без JS. Toggle pill с rotate(180°).
  - `CtaBanner.astro` — финальный оранжевый CTA «Готовы к отдыху?» с белой кнопкой.
  - `CookieBanner.astro` — island: localStorage `ps_cookie_consent` (`accepted` | `necessary`), TTL 12 мес, RAF-reveal при первом визите, кнопки «Согласен» + «Только необходимые».
- Страницы (`src/pages/`):
  - `index.astro` — главная со всеми 8 блоками в порядке SCOPE §1.
  - `destinations/index.astro` — агрегатор 5 направлений.
  - `destinations/[slug].astro` — `getStaticPaths()` для 5 destinations с intro, фичи, страны, 3-шаговый «Как заказать», CTA.
  - `tours/index.astro` — список 4 туров.
  - `tours/[slug].astro` — детальная страница тура (фото с бейджем/рейтингом + 4-col meta grid + hook + описание + фичи + disclaimer).
  - `privacy.astro`, `cookies.astro`, `agreement.astro` — 152-ФЗ политики, адаптированы из `01_CLIENT_AND_SCOPE/SITE_LEGAL/01-03`.
  - `404.astro` — кастомная 404.
- Публичные ассеты:
  - `public/robots.txt` — `User-agent: *, Allow: /, Sitemap: https://pod-solncem.ru/sitemap-index.xml`.
  - `public/favicon.svg` — копия `04_RESEARCH_AND_DESIGN/01_SITE_DESIGN/logo-mark.svg`.
  - `netlify.toml` — `build.command = "npm run build"`, `publish = "dist"`, security headers (X-Frame-Options SAMEORIGIN, X-Content-Type-Options nosniff, Strict-Transport-Security, Referrer-Policy strict-origin-when-cross-origin, Permissions-Policy), cache-immutable для `/_astro/*`.
  - `.env.example`, `.env`, `.gitignore` (включает `dist/`, `node_modules/`, `.env`, `.astro/`).
- README.md — инструкции dev/build/preview, структура папок, ссылка на `tMeLink()`, перечень «что НЕ сделано и почему».
- Доказательства:
  - `npm run check`: 35 файлов, **0 errors / 0 warnings / 0 hints**.
  - `npm run build`: **16 страниц** в `dist/`, 610 КБ total, EXIT=0. Sitemap `dist/sitemap-index.xml` + `dist/sitemap-0.xml` сгенерированы, `dist/robots.txt` на месте.
  - Скриншоты `09_TESTING_AND_RELEASE/screenshots/2026-09-site/` — главная 320 / 390 / 430 / 1440, 4 страницы туров на 320, cookie баннер на 320 и 1440.
  - Записи в `09_TESTING_AND_RELEASE/EVIDENCE_LOG.md` (строки 19–25).

**Что не сделано и почему:**

| Что | Почему |
|---|---|
| Реальные фото направлений и туров | Не предоставлены Сергеем (OPEN_QUESTIONS_TO_SERGEY, сессия 17–18.09). В `Hero.astro` и `ToursCarousel.astro` стоят CSS-градиенты с цветовой палитрой направления. Файлы помечены для замены в коде. |
| Реальные цены на туры (89/145/198/58 тыс ₽) | Гипотезы по типичной рыночной практике, помечены в коде `// TODO(sergey)` и в туре есть disclaimer «Гипотеза, требует подтверждения». |
| Имя менеджера «Алина», «20+ стран опыта» | Гипотеза из OpenQuestion #2 к Сергею. Помечено плашкой «гипотеза, требует подтверждения». |
| Реальные телефон +7 (495) 123-45-67 и email info@pod-solncem.ru | Заглушки из `REQUISITES.md`, помечены `// TODO(sergey)` в `src/consts/site.ts`. |
| Юридический review 3 политических страниц | Не было юриста. Тексты взяты из `01_CLIENT_AND_SCOPE/SITE_LEGAL/{01,02,03}*.md`, адаптированы для web. Каждая страница содержит блок «Юридический review требуется до публичного запуска». |
| Реальный фотопортрет менеджера | Не предоставлен. Плейсхолдер — круг с белым фоном и буквой «А». |
| Реальные фото менеджера + hero-sea | Hero — CSS-градиент «закат» с декоративным солнечным кругом; manager — placeholder-аватар. Замена 1-к-1 через замену блока с градиентом на `<img>` (комментарий TODO в коде). |
| ID Яндекс.Метрики | Заглушка `00000000` в `.env`. Метрика НЕ загружается пока ymId не станет числом. См. `BaseLayout.astro`. |
| Git commit | Запрещено без явного разрешения Павла. |
| Деплой на Netlify | Отложено: требует (а) commit, (б) DNS pod-solncem.ru прописать, (в) решить GitHub repo `site-marketing`. Делает Raekwon в Э9. |
| Lighthouse ≥ 90 мобильный | Не замеряли — требует полноценного рантайма в браузере. Файлы на месте, шрифты — Google Fonts с preload, тени — минимальные, JS — только CookieBanner + drawer. |
| SEO meta `og:image` для соцсетей | По умолчанию `/favicon.svg`. Потребует настоящих preview-картинок. |

**Состояние артефактов сессии 18.09.2026:**

| Артефакт | Путь | Размер | Статус |
|---|---|---|---|
| Репозиторий сайта | `D:\ТУРИЗМ СЕРГЕЙ\07_CODE\site-pod-solncem` | 39 файлов | собран, `dist/` 610 КБ |
| Скриншоты | `09_TESTING_AND_RELEASE/screenshots/2026-09-site` | 11 PNG | записаны |
| Лог build | `09_TESTING_AND_RELEASE/logs/2026-09-18-astro-build.log` | 2.6 КБ | EXIT=0, 16 страниц |
| Лог typecheck | `09_TESTING_AND_RELEASE/logs/2026-09-18-astro-check.log` | 432 байт | 0/0/0 |
| Записи в EVIDENCE_LOG | `09_TESTING_AND_RELEASE/EVIDENCE_LOG.md` | +8 строк | добавлены |

**Следующий шаг (один):**
- Если Павел разрешил commit → закоммитить `07_CODE/site-pod-solncem` в новый приватный репо `site-marketing` на GitHub, поднять на Netlify free tier, прописать DNS `pod-solncem.ru` (см. `SITE_ARCHITECTURE.md §5`).
- Если commit ещё не разрешён → держать репозиторий локально. Э9 (Raekwon) выполняет деплой сам, когда получит доступ.