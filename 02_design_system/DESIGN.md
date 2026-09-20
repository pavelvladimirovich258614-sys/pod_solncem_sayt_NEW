---
version: alpha
name: "Под Солнцем"
description: "Туристическое агентство — тёплая editorial-эстетика, тёмно-синий serif-заголовок на тёплом кремовом фоне, оранжевый CTA, рукописная подпись как тёплый акцент."
colors:
  primary: "#0F172A"
  secondary: "#475569"
  muted: "#5B6470"
  accent: "#C8420F"
  accentHover: "#A8360A"
  accentBright: "#F2601B"
  accentSoft: "#FFE9D9"
  surface: "#F8F4F0"
  surfaceCard: "#FFFFFF"
  surfaceDark: "#062537"
  textOnAccent: "#FFFFFF"
  textOnDark: "#F1F5F9"
  border: "#E5DED3"
  borderStrong: "#D1C7B8"
  logoSun: "#F89028"
  star: "#F2B544"
  success: "#1F7A3A"
  info: "#1F6FB5"
  premium: "#7A4FC9"
typography:
  h1:
    fontFamily: "PT Serif"
    fontSize: "44px"
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: "-0.01em"
  h2:
    fontFamily: "PT Serif"
    fontSize: "32px"
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: "-0.005em"
  h3:
    fontFamily: "PT Serif"
    fontSize: "22px"
    fontWeight: 700
    lineHeight: 1.25
  body-lg:
    fontFamily: "Onest"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.55
  body-md:
    fontFamily: "Onest"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.55
  body-sm:
    fontFamily: "Onest"
    fontSize: "13px"
    fontWeight: 400
    lineHeight: 1.5
  caption:
    fontFamily: "Onest"
    fontSize: "12px"
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: "0.02em"
  button:
    fontFamily: "Onest"
    fontSize: "15px"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "0em"
  badge:
    fontFamily: "Onest"
    fontSize: "11px"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "0.04em"
  signature:
    fontFamily: "Caveat"
    fontSize: "26px"
    fontWeight: 400
    lineHeight: 1.1
rounded:
  xs: "4px"
  sm: "8px"
  md: "12px"
  lg: "20px"
  xl: "28px"
  pill: "999px"
spacing:
  xxs: "4px"
  xs: "8px"
  sm: "12px"
  md: "16px"
  lg: "24px"
  xl: "32px"
  xxl: "48px"
  section: "80px"
motion:
  fast: "150ms cubic-bezier(0.4,0,0.2,1)"
  base: "240ms cubic-bezier(0.4,0,0.2,1)"
  slow: "400ms cubic-bezier(0.4,0,0.2,1)"
breakpoints:
  xs: "320px"
  sm: "390px"
  md: "430px"
  lg: "768px"
  xl: "1024px"
  xxl: "1280px"
  xxxl: "1440px"
components:
  button-primary:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.textOnAccent}"
    rounded: "{rounded.pill}"
    padding: "14px 22px"
    typography: "{typography.button}"
  button-primary-hover:
    backgroundColor: "{colors.accentHover}"
    textColor: "{colors.textOnAccent}"
    rounded: "{rounded.pill}"
    padding: "14px 22px"
    typography: "{typography.button}"
  button-primary-active:
    backgroundColor: "{colors.accentHover}"
    textColor: "{colors.textOnAccent}"
    rounded: "{rounded.pill}"
    padding: "14px 22px"
    typography: "{typography.button}"
  button-primary-disabled:
    backgroundColor: "{colors.border}"
    textColor: "{colors.secondary}"
    rounded: "{rounded.pill}"
    padding: "14px 22px"
    typography: "{typography.button}"
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.accent}"
    rounded: "{rounded.pill}"
    padding: "14px 22px"
    typography: "{typography.button}"
  button-secondary-hover:
    backgroundColor: "{colors.accentSoft}"
    textColor: "{colors.accentHover}"
    rounded: "{rounded.pill}"
    padding: "14px 22px"
    typography: "{typography.button}"
  button-outline:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    rounded: "{rounded.pill}"
    padding: "13px 21px"
    typography: "{typography.button}"
  button-outline-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.textOnDark}"
    rounded: "{rounded.pill}"
    padding: "13px 21px"
    typography: "{typography.button}"
  card-tour:
    backgroundColor: "{colors.surfaceCard}"
    textColor: "{colors.primary}"
    rounded: "{rounded.lg}"
    padding: "0"
  card-tour-hover:
    backgroundColor: "{colors.surfaceCard}"
    textColor: "{colors.primary}"
    rounded: "{rounded.lg}"
    padding: "0"
  card-destination:
    backgroundColor: "{colors.surfaceCard}"
    textColor: "{colors.primary}"
    rounded: "{rounded.lg}"
    padding: "0"
  card-review:
    backgroundColor: "{colors.surfaceCard}"
    textColor: "{colors.primary}"
    rounded: "{rounded.lg}"
    padding: "20px"
  card-manager-photo:
    backgroundColor: "{colors.surfaceCard}"
    textColor: "{colors.primary}"
    rounded: "{rounded.lg}"
    padding: "0"
  badge-hit:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.textOnAccent}"
    rounded: "{rounded.pill}"
    padding: "6px 10px"
    typography: "{typography.badge}"
  badge-popular:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.textOnAccent}"
    rounded: "{rounded.pill}"
    padding: "6px 10px"
    typography: "{typography.badge}"
  badge-choice:
    backgroundColor: "{colors.success}"
    textColor: "{colors.textOnAccent}"
    rounded: "{rounded.pill}"
    padding: "6px 10px"
    typography: "{typography.badge}"
  badge-low-price:
    backgroundColor: "{colors.premium}"
    textColor: "{colors.textOnAccent}"
    rounded: "{rounded.pill}"
    padding: "6px 10px"
    typography: "{typography.badge}"
  badge-eyebrow:
    backgroundColor: "{colors.accentSoft}"
    textColor: "{colors.accentHover}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
    typography: "{typography.caption}"
  input-default:
    backgroundColor: "{colors.surfaceCard}"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: "14px 16px"
    typography: "{typography.body-md}"
  input-focus:
    backgroundColor: "{colors.surfaceCard}"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: "14px 16px"
    typography: "{typography.body-md}"
  input-error:
    backgroundColor: "{colors.surfaceCard}"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: "14px 16px"
    typography: "{typography.body-md}"
  accordion-question:
    backgroundColor: "{colors.surfaceCard}"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: "18px 20px"
    typography: "{typography.body-lg}"
  accordion-question-hover:
    backgroundColor: "{colors.surfaceCard}"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: "18px 20px"
    typography: "{typography.body-lg}"
  text-muted-on-surface:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.muted}"
    rounded: "0"
    padding: "0"
  text-muted-on-card:
    backgroundColor: "{colors.surfaceCard}"
    textColor: "{colors.muted}"
    rounded: "0"
    padding: "0"
  input-border-focus:
    backgroundColor: "{colors.surfaceCard}"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: "14px 16px"
    typography: "{typography.body-md}"
  badge-info:
    backgroundColor: "{colors.info}"
    textColor: "{colors.textOnAccent}"
    rounded: "{rounded.pill}"
    padding: "6px 10px"
    typography: "{typography.badge}"
  footer-bg:
    backgroundColor: "{colors.surfaceDark}"
    textColor: "{colors.textOnDark}"
    rounded: "0"
    padding: "48px 24px 24px"
  header-bg:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary}"
    rounded: "0"
    padding: "16px 24px"
---

# Под Солнцем — DESIGN.md

Дата: 18.09.2026 (UTC+08). Верстка: alpha.
Назначение: единая точка истины по визуальной системе нового сайта `pod-solncem.ru`.
Потребители: Masta Killa (Э6, сборка), Copywriter (Э2, тексты), Ghostface (Э7/Э8, юр/SEO-структура — визуальный каркас страниц), Inspectah Deck (QA).

## 1. Brand & Style

Туристическое агентство «Под Солнцем» — тёплая editorial-эстетика с человеческим лицом. Антитеза «корпоративный travel-tech»: тёмно-синие serif-заголовки на тёплом кремовом фоне, фотографии моря и закатов, оранжевый CTA «как солнце», рукописная подпись менеджера как тёплый человеческий акцент.

Стиль опирается на три опоры:

1. **Editorial + travel classic.** Серифные заголовки (PT Serif) создают ощущение глянцевого travel-журнала. Названия стран и заголовки блоков читаются как «заголовок статьи», а не «карточка товара».
2. **Тёплая палитра.** Кремовый фон (#F8F4F0) и оранжевый CTA (#C8420F) — физическое тепло, отсылка к солнцу. Тёмно-синий (#0F172A) для текста — контраст к теплу, читабельность.
3. **Продающая подача без нажима.** Каждый блок отвечает на «почему стоит оставить заявку СЕЙЧАС». Декоративные рукописные подписи «Мир ближе, чем кажется» / «Буду рада помочь!» — единственный разрешённый «эмоциональный» декор; всё остальное — функционально.

Reference-картинка: `D:/ТУРИЗМ СЕРГЕЙ/04_RESEARCH_AND_DESIGN/01_SITE_DESIGN/REFERENCE.png`. Палитра снята пипеткой (см. `dev/extract_palette.py`), шрифты определены визуально как «современный serif + гуманистический sans».

## 2. Colors

Все hex-коды **сняты пипеткой с REFERENCE.png** и **доведены до WCAG AA** без потери тёплого характера. Источник: `dev/extract_palette.py`. Контрасты: `dev/wcag_check.py`.

### 2.1 Палитра — финальная

| Токен | Hex | Роль | Источник |
|---|---|---|---|
| `accent` | `#C8420F` | CTA-кнопка, активные ссылки, акцент в hero/менеджере | Снят с REFERENCE, затемнен для AA |
| `accentHover` | `#A8360A` | Hover/active CTA | Производный от accent |
| `accentBright` | `#F2601B` | Бейджи на фото, рукописный декор, лучи солнца в лого | Точный цвет с REFERENCE |
| `accentSoft` | `#FFE9D9` | Подложка eyebrow-бейджей, hover secondary-кнопки | Производный (осветлён accentBright) |
| `surface` | `#F8F4F0` | Основной фон страницы (cream) | Снят с REFERENCE (n=51804 в топ-30) |
| `surfaceCard` | `#FFFFFF` | Фон карточек, header | Чистый белый (карточки) |
| `surfaceDark` | `#062537` | Фон футера | Снят с REFERENCE (avg dark blue) |
| `textOnAccent` | `#FFFFFF` | Текст на accent-кнопках | — |
| `textOnDark` | `#F1F5F9` | Текст на surfaceDark | — |
| `primary` | `#0F172A` | H1/H2/H3, основной текст, цены | Снят с REFERENCE (near-black) |
| `secondary` | `#475569` | Подзаголовки, важный secondary text | Сланцевый slate-700 |
| `muted` | `#5B6470` | Caption, мета-информация, рейтинг | Настроен для AA на cream |
| `border` | `#E5DED3` | Тонкая граница карточек, divider | Производный от surface |
| `borderStrong` | `#D1C7B8` | Усиленная граница (input-focus, FAQ) | Производный |
| `logoSun` | `#F89028` | Маркер солнца в логотипе (декоративный) | Снят с REFERENCE |
| `star` | `#F2B544` | Заполненная звезда рейтинга | Золотисто-жёлтый |
| `success` | `#1F7A3A` | Бейдж «Выбор туристов» (зелёный) | — |
| `info` | `#1F6FB5` | Бейдж «Популярно» (синий, если потребуется) | — |
| `premium` | `#7A4FC9` | Бейдж «Низкая цена» (фиолетовый) | — |

### 2.2 Контрасты (WCAG AA — все тексты проходят)

| Пара | Ratio | AA-normal | AA-large |
|---|---|---|---|
| `text-primary` на `surface` | 16.31 | PASS | PASS |
| `text-primary` на `surfaceCard` | 17.85 | PASS | PASS |
| `text-secondary` на `surface` | 6.92 | PASS | PASS |
| `text-muted` на `surface` | 5.48 | PASS | PASS |
| `text-on-dark` на `surface-dark` | 14.44 | PASS | PASS |
| `text-on-accent` на `accent` | 4.95 | PASS | PASS |
| `text-on-accent` на `accentHover` | 6.57 | PASS | PASS |
| `text-primary` на `accent-soft` | 15.23 | PASS | PASS |

**Отступление от REFERENCE.** Точная оранжевая с REFERENCE (#F2601B) даёт контраст 3.25:1 с белым — **не проходит AA-normal**. Поэтому `accent` (кнопочный) затемнён до `#C8420F`. Точный цвет с картинки сохранён как `accentBright` и используется только для декоративных бейджей и лучей солнца (где надписи выполнены белым на полупрозрачной плашке/контрастном фоне). Это сознательная accessibility-коррекция, зафиксированная в комментарии к `accentBright`.

### 2.3 Где какой цвет

- **Заголовки H1/H2/H3** → `primary` (`#0F172A`)
- **Цены в турах** → `primary` (жирный serif), символ ₽ можно оставить `accentBright` для теплоты (≥18px, large text — AA passes)
- **CTA-кнопки** → фон `accent`, текст `textOnAccent`. На hero — крупная primary CTA (≥44px tall)
- **BORDER на белых карточках** → нет, только тень `elevation.card`. На кремовом фоне — `border`
- **Header** → фон `surface` (cream), sticky top, тонкая нижняя граница `border`
- **Footer** → фон `surfaceDark`, текст `textOnDark`, CTA-кнопка подписки — `accent`
- **Рейтинг звёзды** → `star` (декоративно, не текст — WCAG не применяется)
- **Лого-солнце** → `logoSun` (декоративно)

## 3. Typography

**Пары шрифтов:**
- **Заголовки (H1–H3), цены, названия стран/туров:** `PT Serif` (Google Fonts, бесплатный, идеальная кириллица). Чуть сжатый по сравнению с Source Serif, но легче Lora.
- **Тело текста, кнопки, навигация, подписи:** `Onest` (Google Fonts, автор — Миша Крылов, отличная кириллица, современный гротеск). Manrope/Inter — запасные варианты, если Onest не загрузится.
- **Декоративные рукописные подписи** («Мир ближе, чем кажется», «Буду рада помочь!»): `Caveat` (Google Fonts). Альтернатива — Yellowtail (хуже кириллица).

### 3.1 Шкала (mobile-first, 320 px — base)

| Уровень | Семейство | Размер / line-height | Weight | Letter-spacing | Где используется |
|---|---|---|---|---|---|
| `h1` | PT Serif | 44px / 1.10 | 700 | -0.01em | Hero главной. На десктопе ≥1280 — 56px |
| `h2` | PT Serif | 32px / 1.15 | 700 | -0.005em | Заголовки секций («Подберём отдых под вас», «Туры, которые стоит посмотреть»). На десктопе — 40px |
| `h3` | PT Serif | 22px / 1.25 | 700 | 0 | Заголовки карточек (название страны, имя менеджера) |
| `body-lg` | Onest | 17px / 1.55 | 400 | 0 | Подзаголовок hero, лид-абзацы |
| `body-md` | Onest | 15px / 1.55 | 400 | 0 | Описания карточек, основной текст |
| `body-sm` | Onest | 13px / 1.50 | 400 | 0 | Мета-информация («7 ночей», «вылет из Москвы») |
| `caption` | Onest | 12px / 1.40 | 500 | 0.02em | Eyebrow-бейджи, подписи под фото |
| `button` | Onest | 15px / 1.20 | 600 | 0 | Текст в кнопках |
| `badge` | Onest | 11px / 1.00 | 700 | 0.04em | Бейджи («Хит продаж», «4.9») — uppercase опционально |
| `signature` | Caveat | 26px / 1.10 | 400 | 0 | Декоративные рукописные подписи |

### 3.2 Иерархия типографики — что считать крупным

- На мобиле (≤430px): H1 ≥ 36px, цены ≥ 22px, CTA ≥ 17px
- На десктопе (≥1024px): H1 ≥ 48px, цены ≥ 26px
- Контраст минимум 4.5:1 для обычного текста, 3:1 для крупного (≥18px regular или ≥14px bold)

### 3.3 Подключение (HTML)

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@400;700&family=Onest:wght@400;500;600;700&family=PT+Serif:wght@400;700&display=swap" rel="stylesheet">
```

### 3.4 Fallback-стек

```css
font-family: "PT Serif", Georgia, "Times New Roman", serif;
font-family: "Onest", -apple-system, BlinkMacSystemFont, "Segoe UI", system-ui, sans-serif;
font-family: "Caveat", "Bradley Hand", "Comic Sans MS", cursive;
```

## 4. Layout & Spacing

Сетка — **4 pt**, mobile-first. Базовая единица = 4px. Все размеры — кратные 4.

### 4.1 Spacing scale

| Токен | px | Назначение |
|---|---|---|
| `xxs` | 4 | Расстояние между иконкой и текстом в одной строке |
| `xs` | 8 | Расстояние между элементами внутри карточки (иконка → подпись) |
| `sm` | 12 | Padding мелких кнопок, gap в trust-бейджах |
| `md` | 16 | Стандартный padding карточки, gap между карточками в горизонтальном списке |
| `lg` | 24 | Padding секции по бокам (mobile), gap между крупными блоками |
| `xl` | 32 | Padding секции по бокам (tablet), вертикальный gap |
| `xxl` | 48 | Padding секции (desktop), расстояние между крупными секциями |
| `section` | 80 | Вертикальный padding между секциями (desktop), 64 на mobile |

### 4.2 Breakpoints

| Название | px | Поведение |
|---|---|---|
| `xs` | 320 | Базовый mobile. Помещается всё без горизонтального скролла. |
| `sm` | 390 | iPhone 12/13/14/15. Стандартный mobile. |
| `md` | 430 | iPhone 15 Plus / 16 Plus. Широкий mobile. |
| `lg` | 768 | Планшет (portrait). 2 колонки в карточках направлений, 2 в турах. |
| `xl` | 1024 | Desktop sm. Сайдбар не появляется, но контент центрируется, max-width 960. |
| `xxl` | 1280 | Desktop md. Контент 1184. Хедер показывает все ссылки меню. |
| `xxxl` | 1440 | Desktop lg. По референсу. Контент 1320. |

### 4.3 Контейнеры

- Mobile (≤430px): горизонтальные отступы 16px, контент edge-to-edge
- Tablet (768): отступы 24px
- Desktop (≥1024): отступы 32px, контейнер центрируется, max-width по таблице выше

### 4.4 Сетки секций (grid-template-columns)

- **Trust-бейджи (3 шт)**: mobile `1fr`, tablet `repeat(3, 1fr)`, desktop `repeat(3, 1fr)`
- **Направления (5 шт)**: mobile `1fr`, tablet `repeat(2, 1fr)`, desktop `repeat(5, 1fr)`
- **Туры (4 шт)**: mobile `1fr`, tablet `repeat(2, 1fr)`, desktop `repeat(4, 1fr)`
- **Отзывы (6 шт)**: mobile `1fr`, tablet `repeat(2, 1fr)`, desktop `repeat(4, 1fr)` (4 видно, остальные в карусели при клибе)
- **Why-us (4 шт)**: mobile `repeat(2, 1fr)`, desktop `repeat(4, 1fr)`
- **Manager block**: mobile `1fr` (фото сверху, текст снизу), desktop `1fr 1fr` (фото слева)
- **FAQ**: mobile `1fr`, desktop `1fr` (одна колонка по референсу — не аккордеон с иконкой плюс, а pill-list)

## 5. Elevation & Depth

| Уровень | Токен | Сценарий |
|---|---|---|
| `card` | `0 1px 2px rgba(15,23,42,0.04), 0 4px 16px rgba(15,23,42,0.06)` | Карточки туров, направлений, отзывов, менеджера |
| `cardHover` | `0 4px 12px rgba(15,23,42,0.08), 0 12px 32px rgba(15,23,42,0.10)` | Hover карточек (translateY -2px одновременно) |
| `header` | `0 2px 8px rgba(15,23,42,0.04)` | Sticky header при скролле |
| `buttonHover` | `0 6px 16px rgba(200,66,15,0.32)` | Hover primary CTA (оранжевое свечение) |

**Принцип.** Тени — мягкие, двухслойные (close + ambient). Цвет тени = `primary` с малой альфой. Никаких hard shadow.

## 6. Shapes

| Токен | px | Где используется |
|---|---|---|
| `xs` | 4 | Бейджи (`accent-soft` eyebrow), поля ввода |
| `sm` | 8 | Кнопки badge, мелкие элементы |
| `md` | 12 | Карточки отзывов, поля ввода, FAQ-question |
| `lg` | 20 | Карточки туров/направлений/менеджера |
| `xl` | 28 | Hero-photo overlay, модальные окна (запас) |
| `pill` | 999 | Кнопки, бейджи, поля ввода подписки |

Принцип: **скруглы — щедрые**, но не каша. Большинство интерактивных элементов — `pill`. Карточки — `lg`. Изображения внутри карточек — наследуют скругление родителя (через `border-radius` + `overflow:hidden`).

## 7. Components

Все интерактивные элементы обязаны иметь состояния: **default / hover / active / focus-visible / disabled**. Все data-блоки обязаны иметь состояния: **loading (skeleton) / empty / error** — на этапе вёрстки, не «когда-нибудь потом».

### 7.1 Button

#### 7.1.1 Primary (CTA)

Используется для **главного действия** на экране/секции. На главной — «Подобрать отдых за 60 секунд» (hero), «Написать Алине» (менеджер), «Посмотреть тур» (карточка тура), «Подписаться» (футер).

| Состояние | Фон | Текст | Тень | Прочее |
|---|---|---|---|---|
| default | `accent` | `textOnAccent` | — | — |
| hover | `accentHover` | `textOnAccent` | `buttonHover` | translateY(-1px) |
| active | `accentHover` | `textOnAccent` | — | translateY(0), transition 80ms |
| focus-visible | `accent` | `textOnAccent` | — | outline 3px `accentBright` 40%, offset 2px |
| disabled | `borderStrong` | `muted` | — | cursor: not-allowed |

Размеры: padding `14px 22px` (default), `12px 18px` (sm в карточке), `16px 28px` (lg в hero). Min-height **44px** на mobile (touch target).

#### 7.1.2 Secondary (text-style)

Текстовая ссылка-кнопка («Посмотреть туры →», «Все направления →» в hero, «Все отзывы →»).

| Состояние | Фон | Текст | Прочее |
|---|---|---|---|
| default | transparent | `accent` | стрелка → справа |
| hover | `accentSoft` | `accentHover` | translateX(2px) на стрелке |
| focus-visible | `accentSoft` | `accent` | outline `accentBright` |

#### 7.1.3 Outline

Прозрачная кнопка с рамкой (вторичные CTA: «Посмотреть туры» в hero как link).

| Состояние | Фон | Текст | Border |
|---|---|---|---|
| default | transparent | `primary` | 1px `primary` |
| hover | `primary` | `textOnDark` | 1px `primary` |

### 7.2 Card — Tour

Вертикальная карточка 1fr (mobile) → ~250px desktop. Структура:

1. Photo (top, 16:10, rounded-top `lg`): фото страны, бейдж в левом верхнем углу («Хит продаж», «Популярно», «Выбор туристов», «Низкая цена»), рейтинг `★ 4.9 (126 отзывов)` внизу слева на полупрозрачной плашке
2. Body (padding 16px): Country (PT Serif, 22px, `primary`), мета-строка с иконками (`body-sm`, `muted`): «7 ночей · Вылет из Москвы · AI»
3. Цена: «от XXX ₽ на двоих» — `body-sm muted` подпись, число **22px bold serif `primary`**, ₽ можно `accentBright` (≥18px, large)
4. CTA: `button-primary` sm, full-width, «Посмотреть тур →»

**States:** default, hover (translateY(-2px), shadow `cardHover`).

### 7.3 Card — Destination (направление)

Вертикальная карточка, фото сверху без скругления (внутри `lg`-родителя), название + описание снизу.

1. Photo (16:10): пляж/семья/пара/достопримечательность/премиум
2. Body: title (PT Serif, 18px), description (Onest 13px, `muted`, 1-2 строки)
3. Ссылка «Подробнее →» (опционально)

### 7.4 Card — Review

Горизонтальная мини-карточка:

- Аватар 40×40 (round), рядом имя (body-md `primary`) + город (caption `muted`)
- Текст отзыва (body-md `primary`, 3 строки max с ellipsis)
- 5 звёзд `star` под текстом, выровнены слева

### 7.5 Card — Manager Block

Двухколонный блок (mobile stack, desktop side-by-side).

1. Левая колонка: фото менеджера (placeholder, neutral illustration), занимает 100% ширины колонки
2. Правая колонка: цитата в кавычках (PT Serif italic, 22px), 3 буллита (icon + текст), CTA `button-primary lg` «Написать Алине →», декоративная подпись `Caveat` «Буду рада помочь!» + иконка сердечка

### 7.6 Badge

Pill `rounded.pill`, padding 6px 10px, font `badge` (11px bold). Цвета:
- `badge-hit` — `accentBright` + white (для `Хит продаж`)
- `badge-popular` — `accentBright` + white (для `Популярно`)
- `badge-choice` — `success` + white (для `Выбор туристов`)
- `badge-low-price` — `premium` + white (для `Низкая цена`)

### 7.7 Accordion (FAQ)

**По референсу — это НЕ раскрывающийся аккордеон с иконкой +/-, а список-pills**, выровненных в одну колонку. Каждый вопрос в отдельном «pill-card» с тонкой границей `border`. Справа — иконка `+` (24px, `muted`). Клик раскрывает ответ снизу (rotate + → −, smooth height animation 240ms).

States: default / hover (border `borderStrong`) / focus-visible (outline `accentBright`) / open (icon rotated, body shown).

### 7.8 Input / Form

Текстовый input для подписки на влог в футере.

| Состояние | Фон | Border | Текст |
|---|---|---|---|
| default | `surfaceCard` | 1px `border` | `primary` |
| hover | `surfaceCard` | 1px `borderStrong` | `primary` |
| focus | `surfaceCard` | 2px `accent` | `primary` |
| error | `surfaceCard` | 2px `accent` | `accent`, error message под полем `caption` |
| disabled | `surfaceBg` | 1px `border` | `muted` |

Min-height 48px, padding `14px 16px`, radius `md` (12).

### 7.9 Header

Sticky, фон `surface` (cream), высота 72px (desktop) / 64px (mobile), padding `16px 24px`.

Слева: логотип-солнце SVG + «ПОД СОЛНЦЕМ» (PT Serif bold, 18px) + small-caps «ТУРИСТИЧЕСКОЕ АГЕНТСТВО» (caption 11px, `muted`).

Центр (только desktop ≥1024): меню — Туры / Направления / Отели / О нас / Контакты (body-md 15px, `primary`, hover → `accent`).

Справа:
- телефон `+7 (495) 123-45-67` (body-sm `primary`) + подпись «Пн–Вс 9:00–21:00» (caption `muted`) — только ≥768
- CTA `button-primary sm` «Подобрать путешествие →» — только ≥768
- mobile: иконка-бургер (24px, открывает `MobileMenu` — drawer overlay)

При скролле: тень `header` появляется после 100px.

### 7.10 Footer

Тёмный (`surfaceDark`), padding `48px 24px 24px`.

Структура (desktop — 4 колонки, mobile — 1 колонка):

1. Логотип + краткое описание + соцсети (иконки 24×24 inline SVG)
2. Меню (footer): Туры / Направления / Отели / О нас / Контакты
3. Контакты: телефон, email, адрес, график работы
4. Подписка на влог: input + CTA `button-primary sm` «Подписаться»

Нижняя строка: copyright «© 2026 Под Солнцем», ссылки на политики (ПД, Cookie, соглашение).

Цвет ссылок: `textOnDark`, hover → `accentBright`. CTA в подписке — `accent`.

## 8. States — обяз. к дизайну

### 8.1 Data-screen states (loading / empty / error)

Каждый блок с данными на этапе вёрстки должен иметь:

- **Loading:** skeleton-placeholders цвета `border` или `borderStrong`, без shimmer (минимализм). Пример: 4 серых «карточки-призрака» вместо туров.
- **Empty:** иконка-иллюстрация + текст «Пока нет туров в этом направлении» + CTA «Подобрать другой вариант →»
- **Error:** иконка-предупреждение + текст «Не удалось загрузить туры. Попробуйте позже.» + кнопка «Повторить»

### 8.2 Interactive element states

Каждый интерактивный (button, link, card, accordion, input) обязан иметь **default / hover / active / focus-visible / disabled**.

`focus-visible` обязан быть видимым: outline 3px `accentBright` с альфой 0.4 или border 2px `accent`. Без `outline:none` без замены.

## 9. Imagery

- **Hero**: тёплое фото (закат, побережье, пальмы, море). Аспект 21:9 на desktop, 4:3 на mobile. Без overlay-текста на фото (текст вынесен в отдельную колонку).
- **Направления (5)**: 16:10, яркие позитивные сцены. По одному фото на каждое направление.
- **Туры (4)**: 16:10, узнаваемые достопримечательности страны.
- **Менеджер**: портрет, нейтральный фон. До получения от Сергея — neutral illustration placeholder (абстрактный женский силуэт в тёплых тонах).
- **Отзывы**: аватары путешественников (опциональны — если нет, использовать цветные круги с инициалами).
- **Тур-операторы** (в блоке «Почему нам доверяют»): SVG-логотипы на белом фоне.

**Плейсхолдер-стратегия** до получения реальных фото: Unsplash-подобные фото с явной пометкой `placeholder` в коде (через data-атрибут). Готово к замене 1-к-1.

## 10. Iconography

**Inline SVG only.** Никаких emoji-иконок в UI. Набор:

- **Sun-with-rays** — лого (композиция: круг + 8 лучей + волна снизу), цвета `logoSun` + кремовая подложка
- **Arrow-right** — в каждой CTA (14px, в кнопке)
- **Chevron-down** — в FAQ (24px, rotate при open)
- **Calendar** — иконка длительности в карточке тура
- **Plane** — иконка «вылет из Москвы»
- **Fork-knife** (plate) — иконка питания «всё включено»
- **Star** — заполненная (рейтинг) и outline (если когда-то 4/5)
- **Phone** — в хедере/футере
- **Mail** — в футере
- **Telegram** — в соцсетях футера
- **Shield / Document / Lock / People** — в блоке «Почему нам доверяют»
- **Sunburst** — маленький декор рядом с подписью «Мир ближе, чем кажется»

Стиль: stroke 1.5px, round caps, `currentColor`. Размер 16-24px в зависимости от контекста.

## 11. Animation & Motion

| Сценарий | Длительность | Easing |
|---|---|---|
| Hover transitions | 150ms | cubic-bezier(0.4,0,0.2,1) |
| Card lift | 240ms | cubic-bezier(0.4,0,0.2,1) |
| Accordion open | 240ms | cubic-bezier(0.4,0,0.2,1) |
| Page transitions | — | не используются (статический сайт) |
| Skeleton pulse | 1500ms | ease-in-out (subtle 8% opacity) |

**`prefers-reduced-motion: reduce`** — все `transform` отключаются, длительности → 0.01ms.

## 12. Логотип

Логотип-солнце — inline SVG, отрисован вручную по мотивам референса:

- Внешний круг (солнце), 8 треугольных лучей, цвет `logoSun` (`#F89028`)
- Под солнцем — стилизованная волна (`accentBright`, 2 линии)
- Справа от маркера — текст «ПОД СОЛНЦЕМ» (PT Serif bold, uppercase, 18px), под ним small-caps «туристическое агентство» (caption 11px)

Файл: `dev/logo-sun.svg`. Доступен в 2 вариантах: цветной (для header/footer) и монохромный (для favicon).

## 13. Do's and Don'ts

### Do

- Следовать 4pt grid, все размеры кратны 4
- Использовать semantic tokens (`accent`, `surface-bg`), не raw hex в компонентах
- Писать `outline` для focus-visible на каждом интерактивном элементе
- Снабжать каждую data-картинку `alt` текстом (на русском)
- Использовать `currentColor` в inline SVG для иконок
- Тестировать контраст в DevTools перед merge
- Использовать Telegram deep-link для всех CTA: `https://t.me/pod_solncem_travel_bot?start=<source>`

### Don't

- Не использовать `accentBright` (#F2601B) для кнопок с белым текстом — не проходит AA
- Не использовать emoji как иконки в UI
- Не использовать `rounded-full` (=pill) везде — это для кнопок и бейджей, карточки должны быть `lg`
- Не использовать `rounded-2xl` на всём (анти-паттерн)
- Не использовать glassmorphism без причины
- Не использовать Inter/Roboto по инерции — мы выбрали PT Serif + Onest осознанно
- Не использовать purple/blue gradient на всём
- Не использовать placeholder lorem ipsum — контент должен быть реальным (российские направления, реальные форматы)
- Не ставить glassy/shadowy обводки там, где можно обойтись тонкой линией `border`
- Не ломать mobile-first: 320px — базовый, всё помещается без горизонтального скролла

## 14. Структура файлов в репозитории (для Masta Killa)

```
src/
├── styles/
│   └── global.css                  # Tailwind v4 @theme block с этими токенами
├── consts/
│   ├── tokens.ts                   # TS-копия токенов (синхронизировано с global.css)
│   ├── sources.ts                  # telegram deep-link source enum
│   └── site.ts                     # SITE_NAME, SITE_PHONE, ...
└── components/
    ├── Header.astro                # использует токены accent/surface
    ├── Hero.astro                  # H1 + 2 CTA + декор-подпись
    ├── TrustBadges.astro           # 3 бейджа
    ├── DestinationsGrid.astro      # 5 карточек
    ├── ToursCarousel.astro         # 4 тура
    ├── ManagerBlock.astro          # Алина + цитата + буллиты
    ├── Reviews.astro               # 6 отзывов
    ├── WhyUs.astro                 # 4 пункта
    ├── Faq.astro                   # 5-7 вопросов
    ├── CtaBanner.astro             # финальный CTA
    ├── Footer.astro                # тёмный, подписка
    ├── CookieBanner.astro          # 152-ФЗ
    ├── MobileMenu.astro            # drawer
    └── SeoHead.astro               # meta/og
```

## 15. Известные ограничения

- **Фото менеджера** — placeholder (нейтральная иллюстрация). Реальное фото ждём от Сергея (OPEN_QUESTIONS_TO_SERGEY.md №2).
- **Цены в турах «от XXX ₽»** — гипотетические значения. Подтверждение от Сергея (OPEN_QUESTIONS_TO_SERGEY.md).
- **Телефон +7 (495) 123-45-67** и **email info@pod-solncem.ru** — заглушки из REFERENCE. Подтверждение от Сергея (№1).
- **Имя менеджера «Алина»** — гипотеза. Подтверждение от Сергея (№2).
- **Точные hex палитры** — сняты пипеткой с REFERENCE, **доведены до WCAG AA**. Точная `accentBright` сохранена для декора.
- **ID Яндекс.Метрики** — ставим с placeholder ID (заменит Сергей).

## 16. Что проверит Inspectah Deck (QA)

1. Палитра: все цвета — из `colors:`, ни одного raw hex в компонентах.
2. Контраст: каждый текст ≥4.5:1 (large ≥3:1) на своём фоне. Проверять в DevTools.
3. Мобиль 320px: всё помещается без горизонтального скролла.
4. Шрифты: PT Serif для заголовков и цен, Onest для всего остального, Caveat для рукописных.
5. Сетка: 4pt grid (все размеры кратны 4).
6. Кнопки: focus-visible outline есть и виден.
7. CTA: все ведут на `https://t.me/pod_solncem_travel_bot?start=<source>` (проверить вручную).
8. Лого: SVG, не PNG, не emoji.
9. Бейджи туров: все 4 варианта («Хит продаж», «Популярно», «Выбор туристов», «Низкая цена») присутствуют на странице.
10. Декоративные подписи «Мир ближе, чем кажется» и «Буду рада помочь!» присутствуют.
