# SITE_ARCHITECTURE: сайт «Под Солнцем»

Дата: 18.09.2026 (UTC+08).
Основание: SCOPE.md (USER_DIRECTED), OPEN_QUESTIONS_TO_SERGEY.md.
Назначение: фиксирует технический стек и устройство репозитория для нового сайта `pod-solncem.ru` (замена kupit-tyr.ru).

---

## 1. Выбранный стек

| Слой | Решение | Почему именно это |
|---|---|---|
| **Генератор страниц** | **Astro 5.x** (static output) | Контент-первый сайт (20 статичных страниц + 9 изолированных интерактивных островков). Astro рендерит HTML по умолчанию, в браузер летит **0 КБ JS** на страницах без островов и только нужный runtime на страницах с ними. Идеально для Core Web Vitals на мобильных. |
| **Стили** | **Tailwind CSS v4** через `@tailwindcss/vite` | Утилитарный CSS, mobile-first из коробки, дизайн-токены через `theme()` в `global.css`. One-click install: `npx astro add tailwind`. |
| **Контент-слой** | **@astrojs/mdx + Content Collections** (typed frontmatter через Zod) | 9 контент-страниц (5 направлений + 4 тура) пишутся как `.mdx` с типобезопасным frontmatter. Copywriter в Э2 редактирует только markdown, не трогает компоненты. |
| **Острова (interactivity)** | Astro islands (`client:visible` / `client:idle`) | Только где реально нужна интерактивность: FAQ-аккордеон, мобильное меню, cookie-баннер, форма подписки на влог. Все остальное — статический HTML. |
| **SEO** | `@astrojs/sitemap` | Автоматический `sitemap-index.xml` + `sitemap-0.xml` на основе роутов + `getStaticPaths()`. `robots.txt` — статический файл в `public/`. |
| **Деплой** | **Netlify** (opensource-tier) | Бесплатный план для opensource-проектов, one-click deploy из Git, глобальный CDN, custom domain через 3 DNS-записи (A/CNAME), автоматический HTTPS через Let's Encrypt, preview-deploys на каждый PR. Совместим со static output Astro без адаптера. Vercel — допустимый запасной вариант, GitHub Pages ограничивает динамические фичи (cookie-баннер с JS всё равно работает, но без serverless). |
| **Шрифты** | Системные (`font-sans` Tailwind) или self-hosted через `@fontsource` | Никаких CDN-зависимостей, GDPR-friendly. |
| **Аналитика** | Яндекс.Метрика — скриптом через `<script>` в `Layout.astro`, ID передаст Сергей |
| **Backend** | **Нет.** Формы → Telegram deep-link (см. § 4). |
| **Хранилище секретов** | `.env` (в `.gitignore`), читается только build-time через `import.meta.env.PUBLIC_*` |
| **Repo** | Новый отдельный репозиторий `site-marketing` в `07_CODE/`, **НЕ сливается** с `frontend-miniapp` и **НЕ** с `telegram-bot` |

### Стек НЕ включает
- Next.js, React Server Components, ISR, Vercel Edge — не нужны, платная функциональность вводится без необходимости.
- Tailwind UI / shadcn / любой платный UI-kit — opensource-only по требованию.
- CMS (Sanity, Strapi, Tilda, Webflow) — тексты хранятся в Content Collections репозитория.
- Node-сервер, SSR, Server Actions — формы обрабатываются Telegram-ботом.

---

## 2. Почему этот стек, а не альтернативы

### Почему НЕ Next.js (App Router)
Next.js — это React-фреймворк, который по умолчанию поставляет React runtime (~90–130 КБ JS до вашего кода) на каждую интерактивную страницу. Даже `output: 'export'` (static) оставляет RSC payload + hydration. Для 20 статичных страниц с 5 изолированными островами это лишний вес. Источники: Vercel (`/i/astro-vs-next-js`), LogRocket (`astro-vs-next-js-ssg-vs-react`), Prerendering (`nextjs-vs-remix-vs-astro-for-seo`, обновлён апрель 2026) — все три источника сходятся на одном: «Astro wins for content-first marketing; Next.js wins for apps». У нас **приложение = визитка** с 5 интерактивными островами (FAQ, меню, cookie, форма влога, галерея). Кроме того, Next.js деплоится «первоклассно» только на Vercel — это привязка к одному вендору. По требованию задачи хостинг должен быть opensource-совместим и не вести на платный SaaS-путь.

### Почему НЕ «чистый HTML + Tailwind на Vite»
Это выглядит как максимально простой вариант, но он теряет ключевые преимущества Astro:
- **Content Collections / MDX** — для 9 контент-страниц (5 направлений + 4 тура) Astro даёт типобезопасный frontmatter (Zod) и автогенерацию `getStaticPaths()` для динамических роутов `/tours/[slug]`. На чистом Vite пришлось бы либо генерировать HTML руками в `node`-скрипте, либо дублировать компонент `<TourLayout>` в 4 копиях.
- **Sitemap-генерация** — `@astrojs/sitemap` сам обходит роуты и кладёт `sitemap-0.xml` в `dist/`. На Vite — ручной плагин или скрипт.
- **SEO meta per page** — `<head>` в Astro пересобирается на уровне layout-а и передаёт `meta` как props. На Vite — `static-render`-обёртки или HTML-partials.
- **Sitemap + robots + canonical + OG** из коробки.

В итоге «чистый Vite» экономит 30 минут на старте, но добавляет дни ручной работы по мере роста контента, и **всё равно не даёт маркетинговых преимуществ** Astro, потому что оба рендерят 0 JS на чистых страницах.

### Что выбрано и почему это правильно
**Astro 5 + Tailwind v4 + MDX** — это та же философия «HTML по умолчанию», что и чистый Vite, плюс контент-слой и экосистема (sitemap, image, integrations), плюс автоматический роутинг по файлам. Идеальный fit для **marketing-сайта с контентными страницами, который хочется отдавать через CDN и не платить за сервер**.

---

## 3. Структура папок (до 2 уровней)

Корень нового репозитория: `D:/ТУРИЗМ СЕРГЕЙ/07_CODE/site-marketing/`.

```
site-marketing/
├── astro.config.mjs             # output: 'static', site: 'https://pod-solncem.ru',
│                                #   integrations: [tailwind(), sitemap(), mdx()]
├── package.json
├── tsconfig.json
├── tailwind.config.ts           # (опционально v4) тема: цвета палитры, шрифты
├── .env                         # PUBLIC_TELEGRAM_BOT_USERNAME=pod_solncem_travel_bot
├── .env.example                 # коммитится, для Copywriter и Deployer
├── .gitignore                   # .env, node_modules, dist, .astro/
│
├── public/                      # статика «как есть» — копируется в dist/ без бандлинга
│   ├── robots.txt               # User-agent: *, Allow: /, Sitemap: https://pod-solncem.ru/sitemap-index.xml
│   ├── favicon.svg              # солнце-лого
│   ├── images/                  # все фото: hero-море, направления (5), туры (4),
│   │                            #   менеджер, отзывы, логотипы туроператоров
│   └── fonts/                   # если self-host через @fontsource (запасной вариант)
│
├── src/
│   ├── env.d.ts                 # типизация import.meta.env.PUBLIC_*
│   ├── styles/
│   │   └── global.css           # @import "tailwindcss"; + :root { --color-accent: #F26B2B; … }
│   │
│   ├── layouts/                 # оболочки страниц (HTML-обвязка, <head>, <Header>, <Footer>)
│   │   ├── BaseLayout.astro     # <html>, meta, SEO, Header, Footer, cookie-banner slot
│   │   └── ContentLayout.astro  # для /tours/[slug] и /destinations/[slug] — узкий hero + контент
│   │
│   ├── components/              # переиспользуемые блоки для главной + 9 контент-страниц
│   │   ├── Header.astro         # лого + меню + телефон + CTA
│   │   ├── Footer.astro         # лого + меню + контакты + email-форма влога
│   │   ├── Hero.astro           # Главная: H1 + 2 CTA + декоративная подпись
│   │   ├── TrustBadges.astro    # 3 бейджа доверия
│   │   ├── DestinationsGrid.astro   # 5 карточек направлений
│   │   ├── ToursCarousel.astro      # 4 тура
│   │   ├── ManagerBlock.astro       # фото Алины + цитата + буллиты
│   │   ├── Reviews.astro            # 6 отзывов
│   │   ├── WhyUs.astro              # 4 пункта доверия
│   │   ├── Faq.astro                # 5–7 вопросов (остров Accordion)
│   │   ├── CtaBanner.astro          # финальный оранжевый CTA на главной
│   │   ├── CookieBanner.astro       # остров: localStorage + (no backend)
│   │   ├── MobileMenu.astro         # остров: drawer
│   │   └── SeoHead.astro            # <title>, <meta description>, canonical, OG
│   │
│   ├── content/                 # === MDX-файлы контента (правит Copywriter в Э2) ===
│   │   ├── config.ts            # Zod-схемы коллекций: destinations, tours, reviews, faq
│   │   ├── destinations/        # 5 файлов: beach.mdx, family.mdx, couple.mdx, …,
│   │   │                        #   premium.mdx — тексты + frontmatter (title, icon, hero, slug)
│   │   ├── tours/               # 4 файла: turkey.mdx, uae.mdx, thailand.mdx, georgia.mdx
│   │   │                        #   frontmatter: price, duration, flightFrom, meal, badge, rating, hero
│   │   ├── reviews/             # 6 .mdx: имя, город, рейтинг 5★, текст
│   │   └── faq/                 # 5–7 .mdx с полями question + answer
│   │
│   ├── pages/                   # === Роутинг = файл (Astro file-based routing) ===
│   │   ├── index.astro          # Главная: собирает все блоки сверху вниз по SCOPE.md §1
│   │   ├── destinations/
│   │   │   ├── index.astro      # все 5 направлений (страница-агрегатор)
│   │   │   ├── [slug].astro     # getStaticPaths() по src/content/destinations/*
│   │   ├── tours/
│   │   │   ├── index.astro      # все 4 тура
│   │   │   ├── [slug].astro     # getStaticPaths() по src/content/tours/*
│   │   ├── blog/                # опционально (не в v1 SCOPE; оставлено пустым)
│   │   ├── privacy.astro        # политика ПД (152-ФЗ)
│   │   ├── cookie.astro         # пояснение cookie
│   │   ├── terms.astro          # пользовательское соглашение
│   │   ├── 404.astro
│   │   ├── robots.txt.ts        # (опционально) @astrojs/robots
│   │   └── sitemap-index.xml    # генерируется @astrojs/sitemap → /dist/
│   │
│   ├── lib/                     # утилиты, чистый TypeScript
│   │   ├── telegram.ts          # t.meLink(source: BlockSource): string → возвращает deep-link
│   │   ├── seo.ts               # buildMeta({title, description, image, canonical})
│   │   └── schema.ts            # Zod-схемы для Content Collections
│   │
│   └── consts/                  # константы
│       ├── tokens.ts            # палитра в TS (синхронизация с global.css)
│       ├── sources.ts           # тип меток блоков CTA: 'hero' | 'manager' | 'callback' | 'newsletter' | …
│       └── site.ts              # SITE_NAME, SITE_PHONE, SITE_EMAIL, SITE_ADDRESS, TELEGRAM_BOT, YM_ID
│
├── scripts/                     # одноразовые скрипты разработки
│   ├── verify-build.mjs         # typecheck + astro check + размер бандла + проверка robots/sitemap
│   └── lighthouse-mobile.mjs    # Lighthouse CI на 320/390/430 (через Playwright/CDP, опционально)
│
└── README.md                    # «как локально поднять», «как деплоить», «как добавить страницу направления»
```

**Уровни в глубину:**
- `src/components/*.astro` — leaf-компоненты, Astro компилирует их в чистый HTML.
- `src/pages/**/*.astro` — entry-роуты; 2 уровня (`pages/destinations/[slug].astro`).
- `src/content/{destinations,tours,reviews,faq}/*.mdx` — контент-файлы по коллекциям.

**Где живёт медиа:** `public/images/` — Next.js-style asset serving, копируется 1-в-1 в `dist/images/`. Все ссылки — абсолютные `/images/hero-sea.webp` или с `astro:assets` для оптимизации (WebP/AVIF, `<picture>`).

**Где живут тексты:**
- Копирайт для 5 направлений + 4 туров + 6 отзывов + 7 FAQ — в `.mdx`-файлах `src/content/.../*.mdx` (правит Copywriter в Э2, согласно SCOPE §3 «принцип продающей подачи»).
- Копирайт главной, шапки, футера, блоков доверия, CTA — захардкожен в `src/components/*.astro` (правят вместе с вёрсткой).

---

## 4. Как формы становятся Telegram deep-link'ами

### 4.1 Схема (без backend, без POST, без email)

```
[Клик на CTA «Подобрать путешествие»]
     │
     ▼
<a href="https://t.me/pod_solncem_travel_bot?start=hero">
     │
     ▼ (браузер → Telegram app / web.t.me)
[Telegram открывает PM с ботом, кнопка «Start»]
     │
     ▼ (пользователь жмёт Start)
[Бот получает Update: /start hero]
     │
     ▼
[Бот знает: источник = "hero" → приветствует «Здравствуйте!
 подбор тура. Опишите, что вы хотите:…»]
```

### 4.2 Контракт deep-link'а (фиксирован)

| Параметр | Значение |
|---|---|
| URL | `https://t.me/{TELEGRAM_BOT}?start={source}` |
| `TELEGRAM_BOT` | `pod_solncem_travel_bot` (из `import.meta.env.PUBLIC_TELEGRAM_BOT_USERNAME`) |
| `source` | строка `[A-Za-z0-9_-]{1,64}`, фиксированный enum (см. ниже). 64 символа — лимит Telegram на payload после `?start=` |
| Кодировка | Прямая (URL-encode `:` и `_` уже безопасны в этом алфавите). base64 НЕ нужен — payload короткие |

**`source`-метки блоков (enum в `src/consts/sources.ts`):**

| Метка | Где используется |
|---|---|
| `hero` | Hero главной (большая оранжевая CTA) |
| `directions` | Блок «Подберём отдых под вас» |
| `tours` | Блок «Туры, которые стоит посмотреть» |
| `manager` | Блок «Ваш менеджер по путешествиям» (Алина) |
| `callback` | Финальный CTA-баннер внизу главной |
| `newsletter` | Email-форма подписки на влог в футере |
| `dest_beach`, `dest_family`, `dest_couple`, `dest_excursion`, `dest_premium` | CTA на страницах направлений |
| `tour_tr`, `tour_uae`, `tour_th`, `tour_ge` | CTA на страницах туров |
| `policy` | Ссылка «…если проблемы в поездке» в FAQ |

### 4.3 Реализация (одна функция, один компонент)

**`src/lib/telegram.ts`**

```ts
import { PUBLIC_TELEGRAM_BOT_USERNAME } from 'astro:env/client';

type BlockSource = 'hero' | 'manager' | 'callback' | …
  // тип из src/consts/sources.ts

export const tMeLink = (source: BlockSource): string =>
  `https://t.me/${PUBLIC_TELEGRAM_BOT_USERNAME}?start=${source}`;
```

**`src/components/Header.astro`** (использование)

```astro
---
import { tMeLink } from '../lib/telegram';
import { SITE_PHONE } from '../consts/site';
---
<a href={tMeLink('hero')}
   class="bg-accent text-white …">
  Подобрать путешествие
</a>
<a href={`tel:${SITE_PHONE}`} class="…">+7 (495) 123-45-67</a>
```

### 4.4 Подписка на влог (отдельный случай — email)

Спецификация говорит «email → та же Telegram-бот-цепочка». Реализация в `src/components/Footer.astro`:

```
Email-форма (input + submit)
     │
     ▼ (JS-остров preventDefault + бот-API)
```

**Вариант A (рекомендуемый, без backend):**
- `<form>` ведёт `action="https://t.me/pod_solncem_travel_bot?start=newsletter"` →
- Telegram-бот при `/start newsletter` отправляет пользователю инструкцию «пришлите ваш email в ответ» →
- Бот сохраняет email в свою БД (она уже у него есть) → запускает цепочку.

**Вариант B (запасной):** внешний opensource сервис — `listmonk` (self-hosted, AGPLv3) на VPS Павла, или `buttondown.com`/`beehiiv` с free-tier — выбирает **Raekwon в Э9**, мы лишь оставляем `action=""` пустым и Raekwon дописывает.

В первом MVP (Э6) идём по варианту A — не требует ничего, кроме правки в `telegram-bot/src/handlers/start.ts`.

### 4.5 Что не делается на сайте

- Нет `POST /api/lead`. Никаких эндпоинтов.
- Нет reCAPTCHA — её функцию выполняет сам факт перехода в Telegram (клик от живого человека).
- Нет cookies для отслеживания источника. `source` уходит в URL-параметре Telegram, не в cookie.
- Нет аналитической воронки на сайте. Яндекс.Метрика даст ретаргетинг, но без событийной модели по CTA.

---

## 5. Деплой на pod-solncem.ru

### 5.1 Целевая конфигурация
| Слой | Что | Где |
|---|---|---|
| Домен | `pod-solncem.ru` (+ `www.pod-solncem.ru`) | Оплачен 07.08.2026, см. `CURRENT_STATE.md` |
| DNS | Текущие NS у домен-провайдера (уточнить у Павла где зарегистрирован) | смотрим `pavel` → `current-registrar` |
| Хостинг | **Netlify** на бесплатном opensource-tier, либо Vercel, либо Cloudflare Pages | см. § 5.3 |
| CDN | Встроен в хостер (Netlify/Vercel — Global Edge) | — |
| TLS | Авто-через Let's Encrypt (Let's → Sectigo у Netlify) | — |
| Build | `npm run build` → `dist/` (~3-5 МБ total, включая ~1.5 МБ оптимизированных фото) | Astro static |
| Repo | GitHub-репо `site-marketing` (приватный, доступ у Павла и команды) | — |
| CI/CD | push в `main` → авто-деплой на production; PR → preview-deploys | — |

### 5.2 DNS-записи на `pod-solncem.ru` (что нужно прописать)

| Тип | Имя | Значение | TTL |
|---|---|---|---|
| CNAME | `www` | `<host>.netlify.app` (или vercel, или cloudflare pages hostname) | 3600 |
| A | `@` | `75.2.60.5` (Netlify load balancer) | 3600 |

Если Netlify: в dashboard включаем «HTTPS» → автоматически получаем сертификат. Домен прописывается в настройках сайта Netlify «Domain management → Add custom domain».

### 5.3 Выбор хостинга (3 валидных варианта)

| Хостинг | Плюсы | Минусы | Рекомендация |
|---|---|---|---|
| **Netlify** (static) | Opensource-tier бесплатный, CDN из коробки, Forms бесплатно (если понадобятся), Atomic deploys, rollback, CLI `netlify-cli` | Vendor-aware (но не vendor-locked как Vercel↔Next) | **Основной вариант.** Один `netlify.toml` + кнопка «Connect to Git» = one-click install за 60 секунд |
| **Vercel** | Идеален для Next.js, для Astro работает (есть `@astrojs/vercel`), Git-based deploys, edge network | Vendor-aware; «first-class» только с Next | Запасной. Если Netlify по политическим причинам не подходит |
| **Cloudflare Pages** | Бесплатный, сеть Cloudflare, opensource-friendly, R2 для больших файлов | Нет preview-комментариев в PR; медленнее билды | Запасной, если нужна интеграция с уже используемым Cloudflare |
| **GitHub Pages** | Бесплатный, один `gh-pages` branch | Только статичный, без env-vars в build, медленная CDN, нет preview на PR | **НЕ рекомендую.** Нет PR-preview'ов — критично для итераций. Нет ENV. |
| **VPS Павла** (ispmanager на reg.ru) | Полный контроль, opensource | Один сервер = одна точка отказа. Не CDN | **НЕ рекомендую.** Сервер и так нагружен (Telegram-бот, Mini App backend). |

**Решение Raekwon (Э9):** основной путь — Netlify static. Один файл `netlify.toml`:

```toml
[build]
  command = "npm run build"
  publish = "dist"

[[headers]]
  for = "/_astro/*"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"
```

### 5.4 Шаги деплоя (для Raekwon, Э9)

1. Создать репо `site-marketing` в организации Павла на GitHub.
2. Залить код (уже без secretов: `.env` в `.gitignore`).
3. На Netlify: «Add new site → Import from Git → выбрать репо → Build command `npm run build`, Publish directory `dist`».
4. В Netlify UI: Site settings → Environment variables → `PUBLIC_TELEGRAM_BOT_USERNAME=pod_solncem_travel_bot`, `PUBLIC_YANDEX_METRIKA_ID=00000000` (поменяет Сергей).
5. Domain settings → Add custom domain `pod-solncem.ru` → Netlify выдаст DNS-записи (см. § 5.2).
6. У регистратора домена `pod-solncem.ru` прописать выданные Netlify DNS-записи.
7. Подождать ~24 ч на DNS-пропагацию, проверить `https://pod-solncem.ru/`.
8. Включить «Force HTTPS», выключить «Public deploy logging».

### 5.5 Локальная разработка

```bash
git clone git@github.com:pavel/site-marketing.git
cd site-marketing
npm install                  # ≈ 250 пакетов, 1.5 минуты
cp .env.example .env         # указать PUBLIC_TELEGRAM_BOT_USERNAME
npm run dev                  # http://localhost:4321
npm run build                # билдит в ./dist/
npm run preview              # локальный preview dist/ на http://localhost:4322
npm run check                # astro check (TypeScript + .astro типы)
```

---

## 6. Соответствие acceptance criteria (из задания)

| Критерий | Где закрыто |
|---|---|
| Один выбранный стек с явным обоснованием | § 1 (таблица) + § 2 (3-абзацное сравнение) |
| Структура папок описана до 2 уровней | § 3, дерево с 2-уровневой глубиной под `src/` |
| Указано, как именно формы становятся Telegram deep-links | § 4, со схемой, контрактом URL, типобезопасной enum, реализацией в одну функцию |
| Указано, как именно деплоится на pod-solncem.ru | § 5, с DNS-записями, шагами Netlify, локальной командой |
| Нет выдумок про платные SaaS | Все решения — opensource или бесплатный tier; каждый платный сервис (Vercel, Netlify, GitHub Pages) — имеет бесплатный opensource-совместимый путь; расписан fallback |

---

## 7. Что передаётся следующим исполнителям (HANDOFF для Э2/Э3/Э6)

**Copywriter (Э2):**
- Писать тексты в `src/content/destinations/*.mdx`, `src/content/tours/*.mdx`, `src/content/reviews/*.mdx`, `src/content/faq/*.mdx`
- Схема frontmatter — в `src/content/config.ts` (заполнит Raekwon параллельно или Ghostface)
- Текст главной, шапки, футера, блоков доверия — **вне зоны**, это в `src/components/*.astro`

**U-GOD (Э3):**
- Палитра (§ 1 «Стек», строка «Tailwind CSS») — точные hex подобрать пипеткой с `REFERENCE.png` и прописать в `src/styles/global.css` (`:root { --color-accent: #…; }`) и в `src/consts/tokens.ts` синхронно.
- DESIGN.md — класть рядом с палитрой.

**Masta Killa (Э6):**
- Поднять Astro-проект по `package.json` (сгенерирован по этому плану), прикрутить все блоки главной в порядке SCOPE.md §1, выкатить 5 + 4 + 3 = 12 content-страниц.

**Raekwon (Э9):**
- Взять § 5 как спецификацию деплоя, поднять на Netlify, привязать `pod-solncem.ru`.

---

## 8. Что нужно от Сергея / Павла ДО старта Э6 (уточнить в Э1 → моём же return)

| Вопрос | Где в плане | Сейчас |
|---|---|---|
| Где зарегистрирован домен `pod-solncem.ru` (reg.ru? beget? другое?) | § 5.2 DNS | Заглушка: «уточнить у Павла» |
| Реальный номер телефона и email в шапке/футере (сейчас заглушки из SCOPE) | `src/consts/site.ts` | Ждём OPEN_QUESTIONS_TO_SERGEY.md §1 |
| Точные hex'ы палитры с REFERENCE.png (или U-GOD подберёт) | § 1, § 7 | `tailwind theme()` из SCOPE §2 — гипотеза |
| Имя менеджера на блок «Алина» (или это плейсхолдер) | Hero `<h2>` | OPEN_QUESTIONS_TO_SERGEY.md §2 |
| ID Яндекс.Метрики (если ставим) | Layout.astro `<script>` | Не критично, можно поставить с placeholder ID |

Всё это — **не блокер для архитектуры**. Архитектура готова, эти поля — декораторы контента, не структуры.
