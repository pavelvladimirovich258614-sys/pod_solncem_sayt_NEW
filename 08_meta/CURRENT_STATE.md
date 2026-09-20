# Фактическое состояние проекта

Дата фиксации: 01.08.2026, дополнено 09.08.2026 по полной переписке с Сергеем 23.07–09.08 (`11_REPORTS/client-dialogue-analysis-09-08-2026.md`).
Все утверждения ниже проверены прямым чтением файлов и Git в день фиксации. Где проверка невозможна, это сказано прямо.

## Дополнение на 09.08.2026: бот развёрнут на сервере

По прямым словам Павла в переписке 09.08.2026 08:44: «Все бота на сервер поставил, сегодня буду фиксить и настраивать самого бота что бы заявки улетали, и прочее». Это меняет статус Telegram-бота: код и runtime теперь физически существуют на сервере, но заявки ещё не отправляются, настройка не завершена. Сервер оплачен 07.08.2026, домен `pod-solncem.ru` выбран в тот же день для Mini App. Тариф сервера: первый из двух предложенных вариантов, 3 месяца за 9 500 ₽ или 6 месяцев за 16 500 ₽.

На ту же дату остаются не переданы Сергеем, хотя запрошены минимум трижды: юзернеймы и имена менеджеров (полностью), текст согласия на обработку персональных данных, ссылки на агрегаторы туров (передан только один, Турвизор).

## Сводка

| Направление | Статус | Доказательство |
|---|---|---|
| Аналитика и исследование | `VERIFIED` | 11_REPORTS, 90_ARCHIVE |
| Проектирование Mini App (IA, User Flow, Wireframes) | `VERIFIED` | 04_RESEARCH_AND_DESIGN |
| Frontend Mini App (код) | `IMPLEMENTED`, не `VERIFIED` | 07_CODE/frontend-miniapp, коммит fc50bc5 |
| Проверки frontend (typecheck/lint/test/build) | `NEEDS_EVIDENCE` | доказательств запуска нет |
| Telegram WebApp integration | `IMPLEMENTED` в виде bridge, не проверено в Telegram | src/hooks/useTelegramWebApp.ts |
| Telegram-бот | учётная запись создана, код не реализован | `@pod_solncem_travel_bot`, отдельный локальный репозиторий `07_CODE/telegram-bot` |
| Backend и хранилище | не существует | в репозитории нет серверного кода |
| HeyGen и ИИ-агенты | `PLANNED`, только проектирование | INTEGRATIONS/HEYGEN в репозитории |
| Контент-система | `PLANNED` | 05_CONTENT |
| Согласование цены с клиентом | `BLOCKED` | 01_CLIENT_AND_SCOPE/BUDGET_AND_ADDITIONAL_WORK.md |

## Git: фактические данные

Единственный репозиторий проекта.

```text
remote origin   https://github.com/pavelvladimirovich258614-sys/pod_solncem.git
ветка           main
HEAD            fc50bc578bfe43e04b220c228862133631e82f52
сообщение       feat: complete Pod Solncem mini app frontend
```

История последних коммитов:

```text
fc50bc5  feat: complete Pod Solncem mini app frontend
0fb6e28  docs: add mini app mobile wireframes
e61c91b  docs: define mini app user flows
690648c  docs: define mini app information architecture
d4a504d  docs: record Pavel's answers to open questions, revert incorrect avatar-name confirmation
b98eb54  docs: add Planetop reference and client design requirements
47a4220  Merge remote-tracking branch 'origin/main'
97f1bec  docs: save checkpoint before Hermes frontend planning
08231c9  Исходное состояние проекта на 31.07.2026
40996f2  Initial commit
```

### Push в GitHub: подтверждён

Вчерашняя команда push сама по себе доказательством не является, поэтому найдено фактическое подтверждение. В файле `.git/logs/refs/remotes/origin/main` рабочей папки `D:\pod-solncem-miniapp-frontend` есть запись:

```text
0fb6e282... fc50bc578...  1785519904 +0800   update by push
```

Запись `update by push` git пишет в reflog remote-tracking ветки только после успешного завершения push. Время: 31.07.2026 17:45:04 UTC. До этого, в 17:33:59 UTC, был `fetch origin main: storing head` на `0fb6e28`.

Прямая проверка через `git ls-remote` из этой среды невозможна: нет учётных данных GitHub, команда завершается ошибкой `could not read Username for 'https://github.com'`. Токен не запрашивался и не запрашивается.

### Расхождение между двумя рабочими копиями

| Копия | HEAD | Комментарий |
|---|---|---|
| `D:\pod-solncem-miniapp-frontend` | `fc50bc5` | актуальная, здесь работал Codex |
| `D:\Claude-Cowork-Kwork` | `0fb6e28` | отстаёт на один коммит, здесь работал Claude |
| `07_CODE/frontend-miniapp` (эта папка) | `fc50bc5` | клон, сделан 01.08.2026 |

Обе исходные папки указывают на один и тот же remote. Это не два проекта, а две рабочие копии одного репозитория. Папка `D:\Claude-Cowork-Kwork` просто не подтягивала последний коммит.

### Незакоммиченные изменения

`git status` в обеих исходных копиях показывает около 103 изменённых файлов. Проверено: это не содержательные правки. Команда `git diff --ignore-cr-at-eol --stat` не выводит ничего, то есть отличаются только символы конца строки (CRLF против LF), появившиеся при работе на Windows. Содержимое файлов идентично.

Вывод: реальных несохранённых правок нет. Коммит и push для их «спасения» не нужны и в рамках этой систематизации не выполнялись.

## Frontend: что реально реализовано

Стек по `package.json`: React 19.2, React DOM 19.2, TypeScript 6.0, Vite 8.2, Vitest 4.1, Testing Library, jsdom, ESLint 10.8.

Команды: `npm run dev`, `npm run build` (внутри вызывает `typecheck`), `npm run lint`, `npm test`, `npm run typecheck`.

Файлы в `src/`:

| Группа | Файлы |
|---|---|
| Экраны (13) | MainScreen, QuizStepOne, QuizStepTwo, QuizStepThree, ReviewScreen, LoadingScreen, ResultsScreen, EmptyScreen, QuestionScreen, ContactsScreen, SendingScreen, SendErrorScreen, SuccessScreen |
| Компоненты | AppHeader, DestinationCarousel, DevPanel |
| Хуки | useTheme, useTelegramWebApp, useDestinationCarousel |
| Библиотеки | lib/storage.ts, lib/validation.ts |
| Данные и типы | data.ts, types.ts |
| Тесты | App.test.tsx, DestinationCarousel.test.tsx |
| Ассеты | 4 логотипа SVG, 4 фото направлений WebP |

Из `README.md` репозитория (написан автором реализации): адаптив под мобильные, светлая и тёмная темы с поддержкой темы Telegram, карусель направлений, пошаговый подбор с сохранением черновика локально, состояния загрузки, пустой выдачи, ошибки отправки и успеха, интеграция с Telegram WebApp API, dev-панель через `?dev=1`, демо-сценарии через `?demo=no-result` и `?demo=network-error`.

Все 13 экранов покрывают 14 спроектированных wireframes WF-01…WF-14.

### Чего в коде нет

- Обращения к серверу. Отправка заявки не уходит наружу.
- Реальных данных подбора. Выдача демонстрационная.
- Настоящего текста согласия на обработку персональных данных.
- Имени ИИ-помощника, оно намеренно не введено.

## Проверки: что есть и чего нет

Есть косвенные доказательства:

- `dist/` присутствует в исходной папке, значит production-сборка хотя бы один раз выполнялась;
- 4 скриншота в `04_RESEARCH_AND_DESIGN/07_DESIGN_HANDOFF`: `destinations-390-light.png`, `destinations-390-dark.png`, `final-light.png`, `final-dark.png`. Подтверждают ширину 390 px и обе темы.

Нет доказательств:

- логов `npm run typecheck`, `npm run lint`, `npm test`, `npm run build`;
- скриншотов ширины 320 px и 430 px;
- запуска внутри Telegram;
- поведения при `prefers-reduced-motion`;
- проверки доступности.

По правилу этого проекта проверка без доказательства не считается пройденной. Поэтому статус frontend `IMPLEMENTED`, а не `VERIFIED`.

## Telegram-бот

1 августа 2026 года по прямому указанию Павла зафиксирован новый отдельный бот:

- название: `Под Солнцем | Подбор туров`;
- username: `@pod_solncem_travel_bot`;
- ссылка: `https://t.me/pod_solncem_travel_bot`.

Локальный репозиторий инициализирован отдельно в `D:\ТУРИЗМ СЕРГЕЙ\07_CODE\telegram-bot`. Remote не добавлен, commit и push не выполнялись. Код и runtime-проверки отсутствуют, поэтому функции бота не имеют статуса `implemented` или `verified`.

Токен хранится только в локальном игнорируемом `.env` этого репозитория как `TELEGRAM_BOT_TOKEN`; его значение, части, маска и хеш не фиксируются в документации и журналах. Frontend и backend остаются отдельными кодовыми базами. `@coral_taganka_bot` не затрагивается.

## Главная архитектурная находка

Репозиторий `pod_solncem` содержит одновременно:

- код клиентского Mini App;
- личную базу знаний Павла: `ABOUT ME/about-me.md`, `ABOUT ME/my-company.md`, `ABOUT ME/anti-ai-writing-style.md`, `TEMPLATES/`;
- все рабочие документы по клиенту, включая `budget.md` (цены, предоплата, внутренние ставки 800/1300/1500 ₽ в час) и `REPORTS/chat-export-analysis-30-07-2026.md` (разбор личной переписки с Сергеем).

Это одна из главных проблем, обнаруженных при систематизации. Если репозиторий публичный, наружу открыты и коммерческие условия Павла, и переписка с клиентом. Проверить публичность из этой среды невозможно. Действие вынесено в `NEXT_ACTION.md` как единственный следующий шаг.

## Деньги, коротко

Получено 5 000 ₽. Пакет B (25 000 ₽, бот плюс ИИ-аватар) не оплачен полностью, остаток 20 000 ₽. Итоговая стоимость выросшего объёма не согласована. Два предложения (PS-01.1 на 10 000 ₽ и PS-01.2 ориентировочно 42 000 ₽) подготовлены, но клиенту не отправлены. Подробно: `01_CLIENT_AND_SCOPE/BUDGET_AND_ADDITIONAL_WORK.md`.
