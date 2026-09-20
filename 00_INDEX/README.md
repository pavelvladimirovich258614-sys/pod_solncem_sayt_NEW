# 📂 Навигация по проекту «Под Солнцем» (ТЗ v1.0)

> Дата: 19.09.2026.
> Назначение: папка для удобной навигации по проекту. Здесь нет смысла держать что-то ещё — всё содержательное в других папках.

## 🚀 С чего начать

| Задача | Куда смотреть |
|---|---|
| Понять что такое проект и что нужно сделать | **`01_TZ/TZ_POD_SOLNCEM_SITE_v1.0.md`** (главный документ, 19 разделов) |
| Прочитать PDF/DOCX вместо markdown | `01_TZ/exports/TZ_POD_SOLNCEM_SITE_v1.0.pdf` / `.docx` |
| Посмотреть как выглядит дизайн | `02_design_system/REFERENCE.png` + `02_design_system/mockups/` |
| Прочитать тексты для блоков | `03_content/blocks/` (8 файлов) |
| Юр.тексты | `04_legal/` (4 файла: политика ПД, cookie, оферта, README) |
| Понять зачем всё и какие вопросы Сергею | `05_scope_and_questions/SITE_SCOPE.md` + `OPEN_QUESTIONS_TO_SЕРГЕЙ.md` |
| Посмотреть образец А Клуб (что брали, что нет) | `06_reference/01_REFERENCE_NOTES_A_KLUB.md` + `06_reference/screenshots/` |
| Понять стек и архитектуру | `07_architecture/SITE_ARCHITECTURE.md` |
| Понять как планировали деплой | `08_deploy_prep/README.md` |
| Что было сделано в сессии | `08_meta/HANDOFF.md` |
| Короткая шпаргалка для ИИ-агента | `08_meta/CONTEXT_FOR_AI.md` |

## 📁 Структура репозитория

```
00_INDEX/                  ← ВЫ ЗДЕСЬ
├── README.md             ← эта навигация

01_TZ/                    ← ГЛАВНОЕ — техническое задание v1.0
├── TZ_POD_SOLNCEM_SITE_v1.0.md
├── SITE_CONTENT_NULL.md  ← Null-документ: всё содержимое сайта блоками (для Claude Design)
└── exports/
    ├── TZ_POD_SOLNCEM_SITE_v1.0.pdf     ← PDF версия ТЗ
    ├── TZ_POD_SOLNCEM_SITE_v1.0.docx    ← DOCX версия ТЗ
    ├── TZ_POD_SOLNCEM_SITE_v1.0.html    ← HTML версия (для браузера)
    └── tz_style.css                     ← CSS для печати ТЗ

02_design_system/          ← Дизайн-система (U-GOD, 18.09)
├── DESIGN.md             ← 40 КБ, 29 компонентов, все токены
├── REFERENCE.png         ← референс-картинка (палитра, блоки)
├── block-map.png         ← аннотированная карта главной
├── exports/
│   ├── tokens.json       ← W3C DTCG формат
│   ├── theme.css         ← Tailwind v4 @theme
│   └── tailwind.theme.json
├── mockups/              ← PNG главной на 320/390/430/1440
├── components/           ← компонентные мокапы (кнопки, карточки, и т.д.)
└── logo/                 ← SVG логотип-солнце

03_content/                ← Все тексты для сайта (Ghostface, 18.09)
├── blocks/                ← 8 файлов: hero, destinations, tours, manager, reviews, faq, trust, seo
├── destinations/          ← 5 страниц направлений (заглушки → см. ТЗ раздел 6)
└── tours/                 ← 4 страницы туров (заглушки → см. ТЗ раздел 7)

04_legal/                  ← 3 страницы-политики (Ghostface, 18.09)
├── 01_privacy_policy.md   ← Политика обработки ПД (152-ФЗ)
├── 02_cookie_consent.md   ← Cookie-уведомление
├── 03_user_agreement.md   ← Пользовательское соглашение
└── README.md              ← что готово, что требует подтверждения

05_scope_and_questions/    ← SCOPE + открытые вопросы Сергею (RZA, 18.09)
├── SITE_SCOPE.md          ← 14.3 КБ — что в объёме, что нет, критерии приёмки
└── OPEN_QUESTIONS_TO_SERGEY.md  ← 5 вопросов (контакты, менеджер, отзывы, юрлицо, партнёры)

06_reference/              ← Анализ сайта «А Клуб» (GZA, 18.09)
├── 01_REFERENCE_NOTES_A_KLUB.md  ← 27 КБ — что берём из образца, что не берём
└── screenshots/           ← 17 скриншотов a-club.ru

07_architecture/           ← Выбор стека и архитектура (GZA, 18.09)
└── SITE_ARCHITECTURE.md   ← 29.6 КБ — Astro 5 + Tailwind v4 + Netlify, deep-link схема

08_deploy_prep/            ← Pre-deploy от Raekwon (19.09)
├── README.md              ← общая карта + TL;DR
├── domains-shortlist.md   ← 5 проверенных доменов
├── deploy-options.md      ← 2 варианта (PaaS vs self-hosted VPS)
├── dns_records.txt        ← шаблоны DNS для 4 хостеров
└── pre-deploy-check.md    ← live vs dist/ расхождение

08_meta/                   ← Handoff, текущее состояние, шпаргалка для ИИ
├── HANDOFF.md             ← финальная запись сессии
├── CURRENT_STATE.md       ← фактическое состояние проекта
└── CONTEXT_FOR_AI.md      ← короткая шпаргалка для следующего ИИ-агента

09_raw_materials/          ← Указатель на сырьё (НЕ включено — слишком большое)
└── README.md              ← что лежит в D:\ТУРИЗМ СЕРГЕЙ\СЫРЬЁ ДЛЯ НОВОГО САЙТА\
```

## 🔍 Как пользоваться этим репозиторием

**Если вы ИИ-агент и нужно понять проект за минимум контекста:**

1. Прочитайте `08_meta/CONTEXT_FOR_AI.md` (короткая шпаргалка).
2. Прочитайте `01_TZ/TZ_POD_SOLNCEM_SITE_v1.0.md` (полное ТЗ).
3. По любому блоку — идите в `03_content/blocks/` за текстом и `02_design_system/` за визуалом.
4. По юр.вопросам — `04_legal/`.
5. По стеку/деплою — `07_architecture/` + `08_deploy_prep/`.

**Если вы Павел и хотите показать Сергею:**

1. Откройте `01_TZ/exports/TZ_POD_SOLNCEM_SITE_v1.0.pdf` (читается как обычный PDF).
2. Откройте `02_design_system/REFERENCE.png` + `mockups/320.png` + `mockups/1440.png` для визуала.
3. Откройте `05_scope_and_questions/OPEN_QUESTIONS_TO_SERGEY.md` и передайте Сергею 5 вопросов.

**Если нужно продолжить работу:**

1. Подтвердите 5 гипотез из `OPEN_QUESTIONS_TO_SERGEY.md`.
2. Получите реальное фото менеджера (или согласие на placeholder).
3. Решите вопрос деплоя (домен + хостинг — см. `08_deploy_prep/`).
4. Когда Сергей утвердит визуал — можно делать commit/push и публиковать.

## ⚠️ Что НЕ подтверждено (гипотезы)

В ТЗ и везде в проекте есть данные, помеченные как **гипотеза**. Они не могут быть опубликованы без явного подтверждения Сергея:

- Цены туров (89/145/198/58 тыс ₽).
- Рейтинги 4.7–4.9.
- Имя менеджера «Алина» (плейсхолдер).
- Телефон, email, адрес.
- Год основания.
- Все 6 отзывов (шаблонные, помечены «образец»).
- Имя ИИ-аватара (Анна/Анастасия) — НЕ вписывать.
- Юрлицо «ООО Под Солнцем» — НЕ выдавать за подтверждённое.
- Банковские реквизиты — НЕ публиковать.

Подробный список: `01_TZ/TZ_POD_SOLNCEM_SITE_v1.0.md` раздел 15.

---

Сессия закрыта 19.09.2026.