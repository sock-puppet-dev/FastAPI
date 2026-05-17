# FastAPI 2026: большой учебник для абсолютного новичка

Актуально на **15 мая 2026** для этого проекта:

- Python: `>=3.12` из `pyproject.toml`
- FastAPI: `0.136.1`
- Pydantic: `2.13.3`
- Starlette: `1.0.0`
- Uvicorn: `0.46.0`
- Управление зависимостями: `uv`
- Текущая точка входа: `main:app`

Этот файл написан как учебник и как шпаргалка одновременно. Его цель - не просто дать команды, а объяснить, **почему FastAPI устроен именно так**, почему используются такие названия, сокращения и теги, и как из одного маленького файла `main.py` вырасти до нормального API-проекта.

Учебник основан на официальной документации FastAPI: **Tutorial - User Guide**, **Advanced User Guide**, **Reference**, **FastAPI CLI** и разделах Deployment. Я не копирую документацию дословно, а пересобираю ее для новичка: проще, подробнее, с объяснением названий, сокращений, ошибок и практических шагов именно для этого проекта.

## Назначение этого гайда

Этот `GUIDE.md` - главный учебный документ проекта. Его задача:

- объяснить FastAPI новичку с нуля;
- перевести ключевые идеи официальной документации на понятный русский язык;
- сохранить английские термины там, где они нужны для чтения документации, кода и ошибок;
- дать строгую структуру обучения;
- показать много маленьких примеров;
- объяснить не только "как написать", но и "почему так называется" и "почему так работает";
- связать каждую важную тему с официальной документацией FastAPI.

Этот чат дальше используется только для работы над этим гайдом: анализа, проверки, улучшения структуры, актуализации по официальной документации и повышения понятности для новичка.

## Как пользоваться этим учебником

Не пытайся читать его как роман за один раз. FastAPI лучше учится руками.

1. Сначала прочитай главы **1-5** и запусти текущий проект.
2. Потом перепиши все маленькие примеры вручную. Не копируй вслепую: печатай сам, запускай, ломай, исправляй.
3. После каждой темы открывай `http://127.0.0.1:8000/docs` и проверяй, как FastAPI понял твой код.
4. Все новые идеи добавляй в `main.py` маленькими шагами: один маршрут, один параметр, одна модель.
5. Когда код станет большим, переходи к главе про структуру проекта и `APIRouter`.
6. Возвращайся к разделу "Словарь и названия" каждый раз, когда встречаешь непонятное сокращение.

Режим обучения:

- **Читать**: понять идею.
- **Писать**: повторить пример.
- **Проверять**: открыть `/docs`, отправить запрос.
- **Объяснять себе**: вслух сказать, что делает каждая строка.
- **Усложнять**: добавить проверку, ошибку, модель, тест.

Если ты можешь объяснить код без подсказки, ты его действительно выучил.

## Быстрая навигация

Если ты открыл учебник впервые, читай так:

1. **Старт**: главы 1-7.
2. **Первый код**: главы 8-16.
3. **Документация и проверка API**: главы 22-23, 45, 47-48.
4. **Архитектура**: главы 13, 17-18, 55, 78.
5. **Практика**: главы 35-38, 65-67 и файл `EXERCISES.md`.
6. **Продвинутые темы**: главы 24-30, 56-64, 71-80.

Если нужно быстро найти тему:

- `Path / Query / Body` - главы 7-8.
- `Pydantic` - главы 9, 73.
- `Ошибки 404/422` - главы 11-12, 45, 54.
- `response_model` - главы 10, 49.
- `Depends` - главы 13, 78.
- `APIRouter` - главы 17-18.
- `Тесты` - главы 22, 59.
- `Безопасность` - главы 28, 58, 79.
- `База данных` - главы 20-21, 56-57.

## Строгая структура учебника

Чтобы учебник был не хаотичной шпаргалкой, а понятным маршрутом обучения, он делится на смысловые части.

| Часть | Главы | Задача |
|---|---:|---|
| A. Ориентация в проекте | 1, 4 | понять файлы проекта, окружение, запуск |
| B. База веба | 2, 5, 6, 7 | понять API, HTTP, URL, path/query/body |
| C. Первый FastAPI-код | 3, 8, 14, 15, 42, 43, 44 | понять приложение, декораторы, типы, функции |
| D. Данные и валидация | 9, 10, 16, 45, 49, 50, 51, 52, 53, 54 | научиться принимать, проверять и возвращать данные |
| E. Документация API | 23, 47, 76 | понять `/docs`, OpenAPI, tags, summary, metadata |
| F. Архитектура | 13, 17, 18, 55, 78 | понять зависимости, роутеры, слои приложения |
| G. Практические возможности | 24, 25, 26, 27, 29, 30, 74, 75, 77, 80 | headers, cookies, forms, files, CORS, middleware, lifespan |
| H. Безопасность и база | 20, 21, 28, 56, 57, 58, 79 | понять БД, миграции, auth, JWT, password hashing |
| I. Качество и production | 22, 32, 33, 59, 60, 61, 62, 63, 64 | тесты, отладка, логи, контракт API, deployment |
| J. Учебная практика | 34, 35, 36, 37, 38, 39, 40, 65, 66, 67, 68, 69, 70 | закрепить знания упражнениями и мини-проектами |
| K. Official-дополнения | 71-80 | темы, которые в документации FastAPI вынесены отдельными страницами |

### Единый формат изучения любой темы

Для каждой новой темы используй один и тот же порядок:

1. **Что это** - короткое определение.
2. **Зачем нужно** - какую проблему решает.
3. **Минимальный пример** - самый маленький рабочий код.
4. **Разбор строк** - что значит каждая строка.
5. **Типичная ошибка** - что чаще всего ломает новичок.
6. **Проверка** - как увидеть результат в `/docs`, браузере, `curl` или тесте.
7. **Связь с official docs** - какой раздел официальной документации читать после этого.

### Правило перевода терминов

В FastAPI нельзя полностью отказаться от английского, потому что код, ошибки, документация и OpenAPI используют английские названия. Поэтому в этом гайде используется формат:

```text
русское объяснение + английский термин в скобках
```

Пример:

- путь (`path`);
- запрос (`request`);
- ответ (`response`);
- тело запроса (`request body`);
- зависимость (`dependency`);
- промежуточный слой (`middleware`);
- схема ответа (`response model`);
- операция пути (`path operation`).

Так новичку понятен смысл по-русски, но он одновременно учит реальные термины, которые встретит в официальной документации.

### Критерии качества этого гайда

Любое будущее улучшение `GUIDE.md` должно проходить по чеклисту:

- тема объяснена с нуля;
- есть русский перевод смысла;
- английский термин сохранен, если он нужен для кода или документации;
- есть минимальный рабочий пример;
- пример можно запустить в этом проекте или легко адаптировать;
- сложные строки разобраны;
- указана типичная ошибка новичка;
- есть способ проверки результата;
- тема не противоречит официальной документации FastAPI;
- если информация зависит от версий, указана дата актуализации;
- структура остается строгой: новая тема попадает в подходящую часть учебника.

Если раздел не проходит этот чеклист, его нужно доработать, а не просто расширять объемом.

## Как этот учебник связан с официальной документацией FastAPI

Официальная документация FastAPI устроена очень грамотно: она ведет от простого `main.py` к полноценному приложению. Этот `GUIDE.md` повторяет ту же логику, но добавляет объяснения "для совсем новичка".

| Официальный раздел FastAPI | Где в этом учебнике | Что ты должен понять |
|---|---:|---|
| Python Types Intro | 41, 44 | зачем FastAPI нужны type hints |
| Virtual Environments | 1, 4 | зачем `.venv`, `pyproject.toml`, `uv.lock` |
| First Steps | 1, 3, 4, 5, 42, 43 | как рождается минимальное приложение |
| Path Parameters | 7, 8, 15, 45 | как FastAPI берет данные из URL |
| Query Parameters | 7, 8, 48, 51 | как работают параметры после `?` |
| Request Body | 7, 9, 16 | как Pydantic-модель становится body |
| Query Validations | 8, 51 | `Query`, `min_length`, `max_length`, `ge`, `le` |
| Path Validations | 8, 15, 16 | `Path`, ограничения чисел, порядок маршрутов |
| Query Parameter Models | 71 | как группировать query-параметры в модель |
| Body - Multiple Parameters | 72 | как принимать path + query + несколько body |
| Body - Fields | 8, 9, 72 | чем `Field` отличается от `Query` |
| Body - Nested Models | 9, 73 | вложенные Pydantic-модели |
| Extra Data Types | 73 | `datetime`, `UUID`, `EmailStr`, `Decimal` |
| Cookie/Header Parameters | 24, 74 | `Cookie`, `Header`, underscore conversion |
| Response Model | 10, 49, 64 | как FastAPI фильтрует и валидирует ответ |
| Response Status Code | 11, 16, 50 | `201`, `204`, `404`, `422` |
| Form Data / Request Files | 24, 75 | формы, файлы, `UploadFile` |
| Handling Errors | 12, 45, 54, 60 | `HTTPException`, `422`, бизнес-ошибки |
| Path Operation Configuration | 23, 47, 76 | `summary`, `description`, `operation_id`, `deprecated` |
| JSON Compatible Encoder | 77 | как превращать модели и даты в JSON-compatible данные |
| Body - Updates | 16, 50 | `PATCH`, `exclude_unset=True`, `model_copy` |
| Dependencies | 13, 55, 78 | `Depends`, sub-dependencies, yield dependencies |
| Security | 28, 58, 79 | OAuth2, Bearer token, password hashing, JWT |
| Middleware | 26, 61, 62 | промежуточная обработка запроса |
| CORS | 25 | почему frontend с другого origin блокируется |
| SQL Databases | 20, 21, 56, 57 | SQL, ORM, session, migrations |
| Bigger Applications | 17, 18, 55 | `APIRouter`, модули, структура проекта |
| Background Tasks | 29 | маленькие задачи после ответа |
| Metadata and Docs URLs | 23, 76 | title/version/docs_url/openapi_url |
| Static Files | 80 | как отдавать CSS/JS/images |
| Testing | 22, 59, 66 | `TestClient`, happy path, ошибки |
| Debugging | 60 | как читать traceback и ошибки |
| FastAPI CLI | 4 | `fastapi dev`, `fastapi run`, `entrypoint` |
| Deployment | 33 | production-чеклист, HTTPS, workers, env |

Как работать с этой таблицей:

1. Выбери тему в официальной документации.
2. Найди соответствующую главу в `GUIDE.md`.
3. Сначала прочитай объяснение здесь.
4. Потом открой официальный раздел и сравни.
5. Перепиши пример руками в `main.py`.

Так ты учишься не "по пересказу", а рядом с официальной документацией.

## 1. Что уже есть в проекте

Структура проекта сейчас очень маленькая:

```text
FASTAPI/
├── main.py
├── tests/
│   └── test_main.py
├── README.md
├── EXERCISES.md
├── GUIDE.md
├── pyproject.toml
├── uv.lock
├── .gitignore
├── .venv/
└── .fastapicloud/
```

### `main.py`

```python
from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Learning",
    version="0.1.0",
    description="Учебное API для пошагового изучения FastAPI.",
)


@app.get("/", tags=["root"], summary="Root endpoint")
def home() -> dict[str, str]:
    return {"message": "Hello from FastAPI Cloud"}


@app.get("/health", tags=["health"], summary="Health check")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/items/{item_id}", tags=["items"], summary="Read one item")
def read_item(item_id: int, q: str | None = None) -> dict[str, int | str | None]:
    return {"item_id": item_id, "q": q}
```

Разбор построчно:

- `from fastapi import FastAPI` импортирует главный класс приложения. `FastAPI` пишется с большой буквы, потому что это класс. Классы в Python обычно пишут в стиле `PascalCase`: каждое слово с большой буквы.
- `app = FastAPI(...)` создает объект приложения. Имя `app` - сокращение от `application`, то есть "приложение". Это стандартное имя, потому что серверу нужно знать, какой объект запускать.
- `title`, `version`, `description` попадают в OpenAPI-документацию и видны на `/docs`.
- `@app.get("/", tags=["root"], summary="Root endpoint")` регистрирует обработчик HTTP-метода `GET` для пути `/`.
- `@` в Python означает **декоратор**. Декоратор оборачивает функцию или регистрирует ее где-то. В FastAPI декоратор говорит: "эта функция отвечает на такой-то HTTP-запрос".
- `get` называется так из-за HTTP-метода `GET`. Он используется, когда клиент хочет **получить** данные.
- `"/"` - корневой путь сайта/API. Его часто называют `root`, потому что это "корень" дерева URL.
- `tags=["root"]` группирует endpoint в документации.
- `summary="Root endpoint"` дает короткое описание endpoint в `/docs`.
- `def home()` объявляет обычную Python-функцию. Имя `home` значит "домашняя страница". В учебниках FastAPI часто используют `read_root`: `read` потому что `GET` читает данные, `root` потому что путь `/`.
- `-> dict[str, str]` - аннотация возвращаемого типа. Она говорит: функция вернет словарь, где ключи - строки и значения - строки.
- `return {"message": "Hello from FastAPI Cloud"}` возвращает Python-словарь. FastAPI автоматически превращает его в JSON.
- `health()` - простой endpoint для проверки, что приложение живо.
- `read_item(item_id: int, q: str | None = None)` показывает официальный базовый паттерн FastAPI: path-параметр `item_id` и необязательный query-параметр `q`.

### `pyproject.toml`

```toml
[project]
name = "fastapi-learning"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "fastapi[standard]>=0.136.1",
    "uvicorn[standard]>=0.46.0",
]

[dependency-groups]
dev = [
    "pytest>=9.0.3",
]

[tool.fastapi]
entrypoint = "main:app"

[tool.pytest.ini_options]
pythonpath = [
    ".",
]
```

Разбор:

- `pyproject.toml` - главный современный файл настроек Python-проекта.
- `TOML` - формат конфигурации. Название исторически расшифровывали как "Tom's Obvious, Minimal Language"; сейчас это "Tom's Obvious Minimal Language".
- `[project]` - секция с метаданными проекта.
- `name` - имя пакета/проекта.
- `version` - версия твоего проекта, не FastAPI.
- `requires-python = ">=3.12"` значит: проект рассчитан на Python 3.12 или новее. FastAPI поддерживает и более старые версии Python, но для учебного проекта выбран современный и достаточно доступный минимум.
- `dependencies` - зависимости, то есть внешние библиотеки.
- `fastapi[standard]` - FastAPI с "standard"-набором дополнительных зависимостей. Квадратные скобки в Python-зависимостях называют **extras**. Это дополнительные возможности пакета.
- `uvicorn[standard]` - Uvicorn с расширенным набором зависимостей для удобного и быстрого запуска.
- `[dependency-groups]` хранит группы зависимостей для разработки.
- `dev` - development, зависимости для разработки, которые не являются частью runtime-логики приложения.
- `pytest` нужен для запуска тестов.
- `[tool.fastapi]` - секция настроек инструмента FastAPI CLI.
- `entrypoint = "main:app"` значит: искать файл `main.py`, а внутри него объект `app`.
- `[tool.pytest.ini_options]` - настройки pytest.
- `pythonpath = ["."]` помогает тестам импортировать `main.py` из корня проекта.

Почему именно `main:app`:

- `main` - имя Python-модуля, то есть файл `main.py` без `.py`.
- `:` отделяет модуль от объекта внутри него.
- `app` - переменная, созданная строкой `app = FastAPI()`.

### `uv.lock`

`uv.lock` фиксирует точные версии всех зависимостей. Это нужно, чтобы проект одинаково устанавливался сегодня, завтра и на другом компьютере.

В этом проекте в lock-файле зафиксированы:

- `fastapi==0.136.1`
- `pydantic==2.13.3`
- `starlette==1.0.0`
- `uvicorn==0.46.0`
- `fastapi-cli==0.0.24`
- `fastapi-cloud-cli==0.17.1`

Почему это важно: `pyproject.toml` говорит "можно версию от такой-то и выше", а `uv.lock` говорит "сейчас реально установлена вот эта конкретная версия".

### `.fastapicloud/`

Эта папка создана при привязке проекта к FastAPI Cloud.

- `cloud.json` содержит `app_id` и `team_id`.
- `.fastapicloud/.gitignore` игнорирует содержимое папки.
- Обычно эту папку не коммитят в публичный репозиторий.

### Остальные служебные файлы и папки

В проекте также есть несколько служебных элементов:

- `README.md` - входная точка проекта: что это, как запустить, где читать учебник.
- `EXERCISES.md` - отдельный файл с практическими заданиями.
- `tests/` - автоматические проверки учебного приложения.
- `.gitignore` - список файлов и папок, которые Git не должен добавлять в историю. Здесь игнорируются `.venv/`, `.idea/`, `.env`, `.DS_Store`, `__pycache__/` и скомпилированные Python-файлы.
- `.venv/` - локальное виртуальное окружение. `venv` - сокращение от `virtual environment`. В нем лежат установленные зависимости проекта.
- `__pycache__/` - cache скомпилированных Python-файлов. Python создает его сам для ускорения импортов.
- `.ruff_cache/` - cache инструмента Ruff, если он запускался в проекте. Ruff используют для linting/formatting Python-кода.
- `.idea/` - настройки JetBrains IDE, например PyCharm. Это настройки редактора, а не логика приложения.

Почему многие служебные папки начинаются с точки:

- в Unix-подобных системах файлы и папки с точкой в начале считаются скрытыми;
- это удобно для настроек, cache и локальных данных инструментов;
- такие элементы обычно не являются частью бизнес-логики приложения.

## 2. Минимальная картина мира: что такое API

**API** расшифровывается как **Application Programming Interface** - программный интерфейс приложения.

Проще:

- пользователь нажимает кнопку в браузере;
- браузер или frontend отправляет HTTP-запрос;
- FastAPI принимает запрос;
- твоя функция обрабатывает данные;
- FastAPI возвращает HTTP-ответ, чаще всего JSON.

Пример:

```text
Клиент: GET /users/1
Сервер: {"id": 1, "name": "Anna"}
```

### Что такое HTTP

**HTTP** - HyperText Transfer Protocol. Это протокол общения клиента и сервера.

HTTP-запрос обычно содержит:

- метод: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`;
- путь: `/users/1`;
- query-параметры: `?limit=10&offset=0`;
- headers: служебные заголовки;
- body: тело запроса, если нужно отправить JSON, форму или файл.

HTTP-ответ обычно содержит:

- status code: `200`, `404`, `422`, `500`;
- headers;
- body, например JSON.

### Самые важные HTTP-методы

| Метод | Что значит | Типичный смысл |
|---|---|---|
| `GET` | получить | прочитать данные |
| `POST` | отправить/создать | создать новый объект или выполнить действие |
| `PUT` | положить целиком | полностью заменить объект |
| `PATCH` | частично исправить | обновить несколько полей |
| `DELETE` | удалить | удалить объект |

Почему такие названия:

- `GET` - "получить".
- `POST` - исторически "отправить сообщение/данные".
- `PUT` - "положить ресурс по адресу".
- `PATCH` - "наложить заплатку", то есть частично изменить.
- `DELETE` - "удалить".

## 3. Что такое FastAPI

FastAPI - это Python-фреймворк для создания API.

Название состоит из двух частей:

- `Fast` - быстрый в разработке и быстрый в выполнении.
- `API` - предназначен именно для программных интерфейсов.

FastAPI стоит на трех главных идеях:

1. **Python type hints**: типы в коде становятся документацией, валидацией и схемой API.
2. **Pydantic**: проверяет входящие и исходящие данные.
3. **Starlette/ASGI**: дает современную асинхронную веб-основу.

FastAPI не "магия ради магии". Он читает твои функции, типы и параметры, а потом строит:

- маршруты;
- валидацию;
- JSON-ответы;
- OpenAPI-схему;
- Swagger UI на `/docs`;
- ReDoc на `/redoc`.

## 4. Запуск проекта

У тебя уже есть `.venv`, `pyproject.toml` и `uv.lock`.

### Проверить версии

```bash
.venv/bin/python -c "import fastapi, pydantic, starlette, uvicorn; print(fastapi.__version__, pydantic.__version__, starlette.__version__, uvicorn.__version__)"
```

Ожидаемая идея результата:

```text
0.136.1 2.13.3 1.0.0 0.46.0
```

### Запустить через FastAPI CLI

Для разработки:

```bash
uv run fastapi dev
```

Если `uv` в песочнице не может читать глобальный cache, локально в терминале проекта команда должна работать нормально. В проекте уже есть:

```toml
[tool.fastapi]
entrypoint = "main:app"
```

Поэтому FastAPI CLI понимает, что запускать.

Для production-запуска:

```bash
uv run fastapi run
```

Разница:

- `fastapi dev` - режим разработки, обычно с reload и удобными настройками.
- `fastapi run` - режим запуска приложения как сервиса.

### Альтернативный запуск через Uvicorn

```bash
uv run uvicorn main:app --reload
```

Разбор:

- `uv run` запускает команду внутри окружения проекта.
- `uvicorn` - ASGI-сервер.
- `main:app` - файл `main.py`, переменная `app`.
- `--reload` перезапускает сервер после изменений кода.

### Что открыть в браузере

После запуска:

- `http://127.0.0.1:8000/` - твой корневой endpoint.
- `http://127.0.0.1:8000/docs` - интерактивная Swagger UI документация.
- `http://127.0.0.1:8000/redoc` - альтернативная документация ReDoc.
- `http://127.0.0.1:8000/openapi.json` - JSON-схема API.

## 5. Главная формула FastAPI

Почти любой endpoint в FastAPI строится по формуле:

```python
@app.method("path")
def function_name(parameters) -> response_type:
    return response
```

Пример:

```python
@app.get("/hello")
def hello() -> dict[str, str]:
    return {"message": "Hello"}
```

Слова:

- `app` - приложение.
- `method` - HTTP-метод: `get`, `post`, `put`, `patch`, `delete`.
- `path` - путь URL.
- `function_name` - имя Python-функции.
- `parameters` - параметры запроса.
- `response_type` - тип ответа.
- `return` - данные, которые FastAPI превратит в HTTP-ответ.

## 6. Словарь сокращений и названий

Это раздел, к которому нужно возвращаться постоянно.

| Термин | Расшифровка | Почему так называется |
|---|---|---|
| API | Application Programming Interface | интерфейс, через который программы общаются |
| HTTP | HyperText Transfer Protocol | протокол передачи гипертекста, потом стал основой веба |
| URL | Uniform Resource Locator | "адрес" ресурса в интернете |
| URI | Uniform Resource Identifier | более общее "имя/идентификатор" ресурса |
| JSON | JavaScript Object Notation | формат данных, похожий на объекты JavaScript |
| ASGI | Asynchronous Server Gateway Interface | стандарт связи async Python-приложения с сервером |
| WSGI | Web Server Gateway Interface | старый синхронный стандарт для Python web |
| CLI | Command Line Interface | интерфейс командной строки |
| CRUD | Create, Read, Update, Delete | четыре базовые операции с данными |
| ORM | Object-Relational Mapper | связывает Python-объекты и таблицы БД |
| DB | Database | база данных |
| SQL | Structured Query Language | язык запросов к реляционным БД |
| JWT | JSON Web Token | токен авторизации в формате JSON-структуры |
| CORS | Cross-Origin Resource Sharing | правила доступа frontend с другого домена |
| TLS | Transport Layer Security | шифрование соединения, основа HTTPS |
| HTTPS | HTTP Secure | HTTP поверх TLS |
| id | identifier | уникальный идентификатор объекта |
| UUID | Universally Unique Identifier | почти уникальный идентификатор |
| DTO | Data Transfer Object | объект передачи данных между слоями |
| OpenAPI | спецификация описания API | стандартная схема endpoints, параметров и ответов |

### Почему функции часто называют `read_items`, `create_user`, `update_item`

В API часто используют CRUD-глаголы:

- `create_*` - создать.
- `read_*` - прочитать.
- `update_*` - обновить.
- `delete_*` - удалить.

Это не обязательно, но удобно:

```python
@app.get("/items")
def read_items(): ...

@app.post("/items")
def create_item(): ...
```

Такие имена читаются как "что делает функция", а не "как она это делает".

### Почему модели называют `UserCreate`, `UserRead`, `UserUpdate`

Один и тот же объект в разных ситуациях имеет разные поля.

Например:

- `UserCreate` - данные, которые клиент отправляет при создании пользователя.
- `UserRead` или `UserPublic` - данные, которые сервер возвращает наружу.
- `UserUpdate` - данные для частичного обновления.
- `UserInDB` - данные, которые лежат в базе, включая служебные поля.

Почему не одна модель `User` на все случаи:

- при создании нужен пароль;
- в ответе пароль возвращать нельзя;
- при обновлении почти все поля могут быть необязательными;
- в базе есть `hashed_password`, `created_at`, `updated_at`.

### Почему `tags=["items"]`

В FastAPI `tags` - это теги OpenAPI-документации. Они группируют endpoints в `/docs`.

```python
@app.get("/items", tags=["items"])
def read_items(): ...
```

Почему `items`, а не `item`:

- тег обычно обозначает раздел API;
- раздел содержит много операций;
- поэтому часто используют множественное число: `users`, `items`, `orders`.

Хорошие теги:

- `users`
- `auth`
- `items`
- `orders`
- `health`

Плохие теги:

- `misc`
- `stuff`
- `api`
- `test`

Тег должен помогать найти нужную группу маршрутов.

## 7. Path, query, body: три главных источника данных

FastAPI определяет источник параметра по месту и типу.

### Path parameter

Path parameter - часть URL.

```python
@app.get("/items/{item_id}")
def read_item(item_id: int) -> dict[str, int]:
    return {"item_id": item_id}
```

Запрос:

```text
GET /items/123
```

`item_id` берется из `{item_id}`.

Почему `{item_id}`:

- фигурные скобки показывают переменную часть пути;
- имя внутри `{}` должно совпадать с параметром функции.

Если открыть:

```text
/items/abc
```

FastAPI вернет `422 Unprocessable Content`, потому что `abc` нельзя превратить в `int`.

### Query parameter

Query parameter идет после `?`.

```python
@app.get("/items")
def read_items(limit: int = 10, offset: int = 0) -> dict[str, int]:
    return {"limit": limit, "offset": offset}
```

Запрос:

```text
GET /items?limit=20&offset=40
```

Почему `limit` и `offset`:

- `limit` - сколько записей вернуть.
- `offset` - сколько записей пропустить.

Это классическая пагинация.

### Body

Body - тело запроса. Обычно это JSON.

```python
from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    price: float

@app.post("/items")
def create_item(item: ItemCreate) -> ItemCreate:
    return item
```

Запрос:

```http
POST /items
Content-Type: application/json

{
  "name": "Keyboard",
  "price": 99.9
}
```

FastAPI понимает: `item` - это Pydantic-модель, значит ее нужно взять из тела запроса.

## 8. `Annotated`, `Query`, `Path`, `Body`

В современном FastAPI лучше использовать `typing.Annotated`.

```python
from typing import Annotated
from fastapi import Query

@app.get("/search")
def search(q: Annotated[str | None, Query(max_length=50)] = None) -> dict[str, str | None]:
    return {"q": q}
```

Что происходит:

- `str | None` говорит Python и FastAPI: значение может быть строкой или `None`.
- `Query(max_length=50)` добавляет правила для query-параметра.
- `Annotated[...]` соединяет тип и метаданные.

Почему `Annotated`:

- слово значит "аннотированный";
- оно позволяет не смешивать сам тип и настройки FastAPI;
- это современный стиль Python typing.

### `Query`

`Query` говорит: параметр берется из query string.

```python
from typing import Annotated
from fastapi import Query

SearchQuery = Annotated[str, Query(min_length=2, max_length=100)]

@app.get("/products")
def search_products(q: SearchQuery) -> dict[str, str]:
    return {"q": q}
```

Почему называется `Query`:

- в URL часть после `?` называется query string;
- значит настройка такого параметра называется `Query`.

### `Path`

`Path` настраивает path-параметр.

```python
from typing import Annotated
from fastapi import Path

@app.get("/items/{item_id}")
def read_item(
    item_id: Annotated[int, Path(ge=1, description="Item ID")]
) -> dict[str, int]:
    return {"item_id": item_id}
```

`ge=1` означает "greater than or equal", то есть `>= 1`.

Частые сокращения в валидации:

- `gt` - greater than, больше чем.
- `ge` - greater than or equal, больше или равно.
- `lt` - less than, меньше чем.
- `le` - less than or equal, меньше или равно.
- `min_length` - минимальная длина строки.
- `max_length` - максимальная длина строки.

### `Body`

`Body` настраивает тело запроса.

```python
from typing import Annotated
from fastapi import Body

@app.post("/echo")
def echo(message: Annotated[str, Body(min_length=1)]) -> dict[str, str]:
    return {"message": message}
```

### `Field`

`Field` - настройка поля внутри Pydantic-модели.

```python
from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=80)
    price: float = Field(gt=0)
```

Разница:

- `Query`, `Path`, `Body` - для параметров endpoint-функции.
- `Field` - для полей Pydantic-модели.

## 9. Pydantic: сердце валидации

Pydantic проверяет данные и превращает их в Python-объекты.

```python
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool = True
```

Почему `BaseModel`:

- `Base` - базовый.
- `Model` - модель данных.
- твой класс наследуется от базовой модели Pydantic и получает валидацию.

### Что делает модель

```python
user = User(id="1", name="Anna")
```

Pydantic попробует привести `"1"` к `int`.

```python
print(user.id)        # 1
print(user.name)      # Anna
print(user.is_active) # True
```

### Основные методы Pydantic v2

```python
user.model_dump()
```

Возвращает словарь.

```python
user.model_dump_json()
```

Возвращает JSON-строку.

```python
User.model_validate({"id": 1, "name": "Anna"})
```

Создает модель из словаря с проверкой.

Почему `model_dump`, а не `dict`:

- в Pydantic v1 часто использовали `.dict()`;
- в Pydantic v2 основное имя - `.model_dump()`;
- название явно говорит: "выгрузить данные модели".

### `ConfigDict`

```python
from pydantic import BaseModel, ConfigDict

class UserPublic(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
```

`from_attributes=True` полезен, когда модель создается из объекта с атрибутами, например ORM-объекта.

Почему `ConfigDict`:

- `Config` - конфигурация;
- `Dict` - словарь;
- в Pydantic v2 конфигурация модели задается словареподобным объектом.

## 10. Response model: что возвращать наружу

`response_model` говорит FastAPI, какой должна быть форма ответа.

```python
from pydantic import BaseModel

class UserInDB(BaseModel):
    id: int
    email: str
    hashed_password: str

class UserPublic(BaseModel):
    id: int
    email: str

@app.get("/users/{user_id}", response_model=UserPublic)
def read_user(user_id: int) -> UserInDB:
    return UserInDB(
        id=user_id,
        email="user@example.com",
        hashed_password="secret-hash",
    )
```

Клиент получит:

```json
{
  "id": 1,
  "email": "user@example.com"
}
```

`hashed_password` не попадет в ответ.

Почему это важно:

- защищает от случайной утечки лишних полей;
- делает документацию точной;
- помогает frontend понимать контракт API.

## 11. Status codes

Status code - числовой результат HTTP-ответа.

| Код | Название | Когда использовать |
|---|---|---|
| `200` | OK | успешный обычный ответ |
| `201` | Created | объект создан |
| `204` | No Content | успешно, но тела ответа нет |
| `400` | Bad Request | плохой запрос клиента |
| `401` | Unauthorized | не прошел аутентификацию |
| `403` | Forbidden | пользователь известен, но доступа нет |
| `404` | Not Found | ресурс не найден |
| `409` | Conflict | конфликт состояния, например email занят |
| `422` | Unprocessable Content | данные синтаксически есть, но не прошли валидацию |
| `500` | Internal Server Error | ошибка сервера |

Пример:

```python
from fastapi import status

@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item() -> dict[str, str]:
    return {"status": "created"}
```

Почему `status.HTTP_201_CREATED`, а не просто `201`:

- число `201` легко забыть;
- именованная константа сама объясняет смысл;
- автодополнение в редакторе помогает выбрать код.

## 12. Ошибки и `HTTPException`

Если ресурс не найден:

```python
from fastapi import HTTPException

fake_items = {1: {"id": 1, "name": "Keyboard"}}

@app.get("/items/{item_id}")
def read_item(item_id: int) -> dict:
    item = fake_items.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
```

Почему `raise`, а не `return`:

- ошибка прерывает обычный поток выполнения;
- FastAPI перехватывает `HTTPException`;
- клиент получает правильный HTTP-ответ.

`detail` - детали ошибки. Обычно это строка или JSON-объект.

```json
{
  "detail": "Item not found"
}
```

## 13. Dependency Injection и `Depends`

Dependency Injection - внедрение зависимостей.

Проще: endpoint говорит, что ему нужно, а FastAPI сам вызывает нужную функцию и передает результат.

```python
from typing import Annotated
from fastapi import Depends

def get_current_user() -> dict[str, str]:
    return {"username": "demo"}

@app.get("/me")
def read_me(
    user: Annotated[dict[str, str], Depends(get_current_user)]
) -> dict[str, str]:
    return user
```

Почему `Depends`:

- endpoint **depends on** something - зависит от чего-то;
- `Depends(get_current_user)` значит: "для этого параметра вызови зависимость `get_current_user`".

Где применяют зависимости:

- подключение к базе данных;
- текущий пользователь;
- проверка токена;
- общая пагинация;
- проверка прав доступа;
- логирование;
- транзакции;
- настройки приложения.

### Зависимость с `yield`

```python
from collections.abc import Generator

def get_resource() -> Generator[str]:
    resource = "opened"
    try:
        yield resource
    finally:
        print("closed")
```

`yield` полезен, когда нужно:

- открыть соединение;
- отдать его endpoint;
- закрыть после ответа.

Для базы данных это классический паттерн.

## 14. `async def` и `def`

FastAPI поддерживает оба варианта.

```python
@app.get("/sync")
def sync_endpoint() -> dict[str, str]:
    return {"mode": "sync"}
```

```python
@app.get("/async")
async def async_endpoint() -> dict[str, str]:
    return {"mode": "async"}
```

Когда использовать `async def`:

- ты вызываешь async-библиотеки;
- async-драйвер базы данных;
- `httpx.AsyncClient`;
- WebSocket;
- много ожидания сети.

Когда использовать обычный `def`:

- простая логика;
- синхронная библиотека;
- CPU-операция;
- ты пока учишься и не используешь async-код внутри.

Главное правило: если внутри endpoint ты пишешь `await`, функция должна быть `async def`.

## 15. Маршруты и порядок

```python
@app.get("/users/me")
def read_current_user() -> dict[str, str]:
    return {"user": "current"}

@app.get("/users/{user_id}")
def read_user(user_id: int) -> dict[str, int]:
    return {"user_id": user_id}
```

Сначала ставь более конкретные маршруты, потом более общие.

Почему:

- `/users/me` - конкретный путь;
- `/users/{user_id}` - переменный путь;
- если перепутать порядок в некоторых роутерах/сценариях, переменный маршрут может перехватить то, что ты считал специальным путем.

Хорошая привычка:

```text
/users/me
/users/{user_id}
```

а не наоборот.

## 16. CRUD пример на памяти

Это учебный пример без базы данных.

```python
from typing import Annotated
from fastapi import FastAPI, HTTPException, Path, status
from pydantic import BaseModel, Field

app = FastAPI()

class ItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=80)
    price: float = Field(gt=0)
    description: str | None = None

class ItemRead(ItemCreate):
    id: int

class ItemUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=80)
    price: float | None = Field(default=None, gt=0)
    description: str | None = None

items: dict[int, ItemRead] = {}
next_id = 1

@app.post("/items", response_model=ItemRead, status_code=status.HTTP_201_CREATED)
def create_item(payload: ItemCreate) -> ItemRead:
    global next_id
    item = ItemRead(id=next_id, **payload.model_dump())
    items[next_id] = item
    next_id += 1
    return item

@app.get("/items", response_model=list[ItemRead])
def list_items() -> list[ItemRead]:
    return list(items.values())

@app.get("/items/{item_id}", response_model=ItemRead)
def get_item(item_id: Annotated[int, Path(ge=1)]) -> ItemRead:
    item = items.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.patch("/items/{item_id}", response_model=ItemRead)
def update_item(item_id: int, payload: ItemUpdate) -> ItemRead:
    item = items.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    update_data = payload.model_dump(exclude_unset=True)
    updated = item.model_copy(update=update_data)
    items[item_id] = updated
    return updated

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int) -> None:
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
```

Разбор важных названий:

- `payload` - "полезная нагрузка" запроса. Так часто называют тело запроса.
- `ItemCreate` - модель входа при создании.
- `ItemRead` - модель ответа.
- `ItemUpdate` - модель частичного обновления.
- `items` - временное хранилище в памяти.
- `next_id` - следующий идентификатор.
- `exclude_unset=True` - выгрузить только поля, которые клиент реально передал.
- `model_copy(update=...)` - создать копию модели с обновленными полями.

Ограничение: данные исчезнут при перезапуске сервера, потому что это память процесса, а не база данных.

## 17. `APIRouter`: когда `main.py` вырос

Когда маршрутов много, их разделяют по файлам.

Пример структуры:

```text
app/
├── main.py
├── routers/
│   ├── users.py
│   └── items.py
└── schemas/
    ├── users.py
    └── items.py
```

`routers/items.py`:

```python
from fastapi import APIRouter

router = APIRouter(prefix="/items", tags=["items"])

@router.get("")
def list_items() -> list[dict[str, str]]:
    return [{"name": "Keyboard"}]
```

`main.py`:

```python
from fastapi import FastAPI
from app.routers import items

app = FastAPI()
app.include_router(items.router)
```

Почему `router`:

- route - маршрут;
- router - объект, который хранит группу маршрутов;
- `APIRouter` - FastAPI-класс для группировки endpoints.

Почему `prefix="/items"`:

- все маршруты внутри файла автоматически начинаются с `/items`;
- не нужно повторять `/items` в каждом декораторе.

Почему `tags=["items"]`:

- все endpoints этого router попадут в группу `items` в `/docs`.

## 18. Рекомендуемая структура учебного проекта

Когда текущий проект станет больше, можно перейти к такой структуре:

```text
FASTAPI/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── deps.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       ├── health.py
│   │       ├── items.py
│   │       └── users.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── security.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── user.py
│   └── services/
│       ├── __init__.py
│       └── users.py
├── tests/
│   └── test_health.py
├── pyproject.toml
├── uv.lock
└── README.md
```

Что где хранить:

- `app/main.py` - создание FastAPI-приложения и подключение роутеров.
- `api/routes/` - HTTP endpoints.
- `api/deps.py` - общие зависимости FastAPI.
- `core/config.py` - настройки.
- `core/security.py` - пароли, токены, безопасность.
- `models/` - ORM-модели базы данных.
- `schemas/` - Pydantic-схемы входа/выхода.
- `services/` - бизнес-логика.
- `tests/` - тесты.

Почему не держать все в `main.py`:

- файл быстро становится длинным;
- сложнее тестировать;
- сложнее искать код;
- сложнее переиспользовать логику.

Но для первых уроков один `main.py` - правильно. Сначала нужно понять основы.

## 19. Настройки через `pydantic-settings`

В `fastapi[standard]` уже входит `pydantic-settings`.

Пример:

```python
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "FastAPI Learning"
    debug: bool = False
    database_url: str = "sqlite:///./app.db"

settings = Settings()
```

Почему настройки выносят:

- разные значения для разработки и production;
- секреты не должны лежать в коде;
- приложение проще переносить.

Почему `.env`:

- `env` - environment, окружение;
- `.env` хранит переменные окружения для локальной разработки;
- `.gitignore` уже игнорирует `.env` и `.env.*`.

Пример `.env`:

```env
APP_NAME="FastAPI Learning"
DEBUG=true
DATABASE_URL="sqlite:///./app.db"
```

В код секреты не коммитят.

## 20. База данных: что нужно понять до ORM

Перед SQLAlchemy или SQLModel важно понять базовые слова:

- `table` - таблица.
- `row` - строка таблицы.
- `column` - колонка.
- `primary key` - главный уникальный ключ.
- `foreign key` - внешний ключ, ссылка на другую таблицу.
- `index` - структура для быстрого поиска.
- `migration` - изменение структуры базы во времени.
- `session` - объект работы с БД в рамках операции.
- `transaction` - группа операций "все или ничего".

Пример таблицы `users`:

| id | email | hashed_password |
|---:|---|---|
| 1 | anna@example.com | hash... |

Почему таблицы часто называют во множественном числе:

- `users` содержит много пользователей;
- `orders` содержит много заказов;
- `items` содержит много товаров.

## 21. SQLModel/SQLAlchemy в FastAPI

FastAPI-документация часто показывает SQLModel для учебных примеров. В production часто используют SQLAlchemy напрямую. Смысл один: Python-классы связываются с таблицами.

Учебная идея модели:

```python
from sqlmodel import Field, SQLModel

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    age: int | None = None
```

Почему `table=True`:

- класс становится не только Pydantic-моделью, но и таблицей БД.

Почему `id: int | None`:

- до сохранения в БД `id` может быть `None`;
- после сохранения база выдаст реальный `id`.

Для твоего проекта SQLModel пока не установлен. Не добавляй базу данных, пока не уверенно понимаешь routes, models, validation, errors и dependencies.

## 22. Тестирование

Тесты нужны, чтобы проверять API автоматически.

FastAPI использует `TestClient`, который построен поверх HTTPX.

Пример `tests/test_main.py`:

```python
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI Cloud"}

def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_item_id_validation_error() -> None:
    response = client.get("/items/not-an-int")
    assert response.status_code == 422
```

Почему `client`:

- это тестовый HTTP-клиент;
- он отправляет запросы в приложение без реального сетевого сервера.

Почему `assert`:

- `assert` проверяет ожидание;
- если ожидание неверное, тест падает.

В этом проекте `pytest` уже добавлен в `dev`-зависимости. Запуск:

```bash
uv run pytest
```

## 23. Документация: `/docs`, `/redoc`, `/openapi.json`

FastAPI автоматически строит документацию.

```python
app = FastAPI(
    title="FastAPI Learning",
    version="0.1.0",
    description="Учебное API для изучения FastAPI",
)
```

Что это дает:

- `title` - название API в документации.
- `version` - версия твоего API.
- `description` - описание.

Endpoint с документацией:

```python
@app.get(
    "/health",
    tags=["health"],
    summary="Health check",
    description="Returns service status.",
)
def health_check() -> dict[str, str]:
    return {"status": "ok"}
```

Почему `summary` и `description`:

- `summary` - короткое описание одной строкой;
- `description` - подробное описание.

Не превращай документацию в роман. Хороший endpoint понятен по:

- пути;
- HTTP-методу;
- тегу;
- имени;
- моделям запроса и ответа.

## 24. Headers, Cookies, Forms, Files

### Header

Header - заголовок HTTP.

```python
from typing import Annotated
from fastapi import Header

@app.get("/agent")
def read_agent(user_agent: Annotated[str | None, Header()] = None) -> dict[str, str | None]:
    return {"user_agent": user_agent}
```

Почему `user_agent`, а не `User-Agent`:

- в Python нельзя удобно назвать параметр `User-Agent`, потому что дефис означает минус;
- FastAPI автоматически конвертирует `user_agent` в HTTP-header `user-agent`.

### Cookie

```python
from typing import Annotated
from fastapi import Cookie

@app.get("/cookie")
def read_cookie(session_id: Annotated[str | None, Cookie()] = None) -> dict[str, str | None]:
    return {"session_id": session_id}
```

Cookie - маленькое значение, которое браузер хранит и отправляет серверу.

### Form

```python
from typing import Annotated
from fastapi import Form

@app.post("/login")
def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
) -> dict[str, str]:
    return {"username": username}
```

Form используется для `application/x-www-form-urlencoded` или `multipart/form-data`, а не для JSON.

### File

```python
from typing import Annotated
from fastapi import File, UploadFile

@app.post("/upload")
def upload_file(file: Annotated[UploadFile, File()]) -> dict[str, str]:
    return {"filename": file.filename}
```

Почему `UploadFile`:

- файл может быть большим;
- `UploadFile` дает потоковый файловый объект и метаданные;
- не нужно целиком держать файл как `bytes`, если это не требуется.

## 25. CORS

CORS нужен, когда frontend и backend находятся на разных origins.

Origin = схема + домен + порт.

Примеры разных origins:

```text
http://localhost:3000
http://localhost:8000
https://example.com
```

Настройка:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

Почему нельзя всегда ставить `allow_origins=["*"]`:

- для публичного read-only API иногда можно;
- для API с cookies, токенами и личными данными это опасно;
- лучше явно перечислять frontend-домены.

## 26. Middleware

Middleware - промежуточный слой между запросом и endpoint.

Схема:

```text
Request -> Middleware -> Endpoint -> Middleware -> Response
```

Пример:

```python
import time
from fastapi import Request

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    duration = time.perf_counter() - start
    response.headers["X-Process-Time"] = str(duration)
    return response
```

Почему `call_next`:

- это функция, которая передает запрос следующему обработчику;
- без нее запрос не дойдет до endpoint.

Middleware используют для:

- CORS;
- логирования;
- измерения времени;
- request id;
- security headers;
- сжатия;
- обработки ошибок.

## 27. Lifespan: старт и остановка приложения

Lifespan - жизненный цикл приложения.

```python
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    print("startup")
    yield
    print("shutdown")

app = FastAPI(lifespan=lifespan)
```

Почему `lifespan`:

- `life` - жизнь;
- `span` - промежуток;
- вместе: время жизни приложения.

Используют для:

- подключения к БД;
- создания HTTP-клиента;
- загрузки ML-модели;
- подготовки cache;
- корректного закрытия ресурсов.

## 28. Авторизация: базовая картина

В API нужно различать:

- Authentication - кто ты?
- Authorization - что тебе можно?

### `401` и `403`

- `401 Unauthorized` - пользователь не доказал, кто он.
- `403 Forbidden` - пользователь известен, но ему нельзя выполнять действие.

Исторически `Unauthorized` звучит как "не авторизован", но в HTTP это чаще про отсутствие/ошибку аутентификации.

### Bearer token

Header:

```http
Authorization: Bearer <token>
```

Почему `Bearer`:

- bearer - "предъявитель";
- кто предъявил токен, тот считается его владельцем;
- поэтому токены нужно защищать как пароль.

Учебная зависимость:

```python
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_token(token: Annotated[str, Depends(oauth2_scheme)]) -> str:
    if token != "dev-token":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token

@app.get("/private")
def private_route(token: Annotated[str, Depends(get_current_token)]) -> dict[str, str]:
    return {"token": token}
```

Это только учебный пример. В реальном проекте:

- пароли хранят только в виде hash;
- JWT подписывают секретом;
- token expiration обязателен;
- refresh-токены проектируют отдельно;
- секреты лежат в environment variables.

## 29. Background tasks

Background tasks - фоновые задачи после ответа клиенту.

```python
from fastapi import BackgroundTasks

def write_log(message: str) -> None:
    with open("log.txt", "a", encoding="utf-8") as file:
        file.write(message + "\n")

@app.post("/send")
def send_message(background_tasks: BackgroundTasks) -> dict[str, str]:
    background_tasks.add_task(write_log, "message sent")
    return {"status": "accepted"}
```

Когда подходит:

- отправить email;
- записать лог;
- маленькая post-processing задача.

Когда не подходит:

- долгие очереди;
- тяжелые задачи;
- надежные фоновые jobs.

Для серьезных задач используют очереди: Celery, RQ, Dramatiq, облачные очереди.

## 30. WebSocket

HTTP - запрос/ответ. WebSocket - постоянное двустороннее соединение.

```python
from fastapi import WebSocket

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket) -> None:
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message: {data}")
```

Когда нужен WebSocket:

- чат;
- live-уведомления;
- игры;
- realtime dashboard.

Когда не нужен:

- обычный CRUD;
- форма регистрации;
- каталог товаров;
- редкие обновления.

## 31. Шаблоны именования

### Python

```python
snake_case = "functions, variables, modules"
PascalCase = "classes"
UPPER_CASE = "constants"
```

Почему:

- так принято в Python PEP 8;
- по имени сразу видно, что перед тобой.

Примеры:

```python
def create_user(): ...

class UserCreate(BaseModel): ...

MAX_PAGE_SIZE = 100
```

### API paths

Хорошо:

```text
/users
/users/{user_id}
/users/{user_id}/orders
/health
```

Плохо:

```text
/getUsers
/user/delete/1
/api/doSomething
```

Почему:

- HTTP-метод уже говорит действие;
- путь должен обозначать ресурс;
- `/users/{user_id}` + `DELETE` понятнее, чем `/deleteUser`.

### Имена параметров

Хорошо:

```python
user_id: int
item_id: int
order_id: int
```

Почему не просто `id`:

- в маленькой функции `id` еще терпимо;
- в большой функции `user_id`, `order_id` яснее;
- `id` еще и имя встроенной функции Python, лучше не затенять без причины.

## 32. Частые ошибки новичка

### Забыть запустить сервер заново

Если нет `--reload`, изменения кода не применятся.

### Перепутать path и query

```python
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None): ...
```

- `item_id` из `/items/123`;
- `q` из `/items/123?q=test`.

### Вернуть пароль наружу

Плохо:

```python
return user_in_db
```

Лучше:

```python
@app.get("/me", response_model=UserPublic)
def read_me() -> UserInDB:
    return user_in_db
```

### Использовать глобальный список как настоящую БД

Для урока можно:

```python
items = []
```

Для реального проекта нельзя:

- данные исчезают;
- несколько процессов не синхронизируются;
- нет транзакций;
- нет надежности.

### Делать все в endpoint

Плохо:

```python
@app.post("/users")
def create_user(...):
    # validate
    # hash password
    # save db
    # send email
    # log
    # format response
```

Лучше разделять:

- endpoint принимает HTTP;
- schema валидирует форму данных;
- service содержит бизнес-логику;
- repository/db слой работает с базой.

## 33. Production-чеклист

Для настоящего deployment:

- использовать `fastapi run` или ASGI-сервер с production-настройками;
- не включать `--reload`;
- хранить секреты в environment variables;
- настроить CORS строго;
- включить HTTPS через платформу/прокси;
- настроить logging;
- иметь healthcheck endpoint;
- иметь тесты;
- иметь миграции БД;
- не возвращать внутренние ошибки клиенту;
- ограничивать размеры upload;
- проверять права доступа;
- следить за зависимостями и обновлениями.

Healthcheck:

```python
@app.get("/health", tags=["health"])
def health() -> dict[str, str]:
    return {"status": "ok"}
```

Почему `health`:

- сервисы мониторинга спрашивают "жив ли сервис?";
- endpoint должен быть быстрым и простым.

## 34. Что учить после базового FastAPI

Порядок:

1. HTTP основы: methods, status codes, headers, cookies.
2. Pydantic v2: models, validation, `Field`, `model_dump`.
3. FastAPI routes: path/query/body, response_model, errors.
4. Dependencies: `Depends`, настройки, DB session.
5. Testing: `TestClient`, pytest, fixtures.
6. Database: SQLModel или SQLAlchemy, migrations.
7. Auth: password hashing, OAuth2, JWT, scopes.
8. Architecture: routers, services, repositories.
9. Deployment: env vars, logs, CORS, healthchecks.
10. Async: когда он нужен и когда нет.

Не прыгай сразу к JWT и базе, если еще путаешь path/query/body. Фундамент здесь важнее скорости.

## 35. Мини-план на 14 дней

### День 1

- Запусти текущий проект.
- Открой `/`, `/docs`, `/redoc`, `/openapi.json`.
- Объясни каждую строку `main.py`.

### День 2

- Добавь endpoints `GET /hello`, `GET /health`.
- Добавь `tags`, `summary`.

### День 3

- Изучи path parameters.
- Сделай `GET /items/{item_id}`.
- Проверь ошибки `422`.

### День 4

- Изучи query parameters.
- Сделай `GET /items?limit=10&offset=0`.

### День 5

- Создай Pydantic-модель `ItemCreate`.
- Сделай `POST /items`.

### День 6

- Добавь `ItemRead`, `ItemUpdate`.
- Сделай `PATCH`.

### День 7

- Добавь `HTTPException`.
- Научись возвращать `404`.

### День 8

- Добавь `response_model`.
- Проверь, что лишние поля не уходят наружу.

### День 9

- Изучи `Depends`.
- Сделай простую зависимость `get_current_user`.

### День 10

- Добавь CORS.
- Разбери, что такое origin.

### День 11

- Добавь `APIRouter`.
- Разнеси `items` в отдельный файл.

### День 12

- Добавь тесты для `/` и `/health`.

### День 13

- Прочитай раздел про настройки.
- Создай `Settings`.

### День 14

- Собери мини-API "Заметки":
  - создать заметку;
  - получить список;
  - получить одну;
  - обновить;
  - удалить.

## 36. Контрольные вопросы

Если можешь ответить без подсказки, тема усвоена.

1. Что такое `app = FastAPI()`?
2. Почему endpoint украшают декоратором `@app.get("/")`?
3. Чем path parameter отличается от query parameter?
4. Когда FastAPI берет данные из body?
5. Зачем нужны Pydantic-модели?
6. Чем `ItemCreate` отличается от `ItemRead`?
7. Что делает `response_model`?
8. Почему нельзя возвращать `hashed_password`?
9. Что такое `Depends`?
10. Когда писать `async def`, а когда `def`?
11. Что такое ASGI?
12. Зачем нужен Uvicorn?
13. Что лежит в `uv.lock`?
14. Почему `main:app` записывается через двоеточие?
15. Что такое OpenAPI?
16. Для чего нужны `tags`?
17. Почему `422` появляется при неверных типах?
18. Что значит `gt`, `ge`, `lt`, `le`?
19. Что такое CORS?
20. Что должно быть в production-чеклисте?

## 37. Идеальный учебный `main.py` после первых тем

Можно использовать как промежуточную цель:

```python
from typing import Annotated

from fastapi import FastAPI, HTTPException, Path, Query, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="FastAPI Learning",
    version="0.1.0",
    description="Учебное API для изучения FastAPI в 2026 году.",
)

class ItemCreate(BaseModel):
    name: str = Field(min_length=1, max_length=80)
    price: float = Field(gt=0)
    description: str | None = None

class ItemRead(ItemCreate):
    id: int

class ItemUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=80)
    price: float | None = Field(default=None, gt=0)
    description: str | None = None

items: dict[int, ItemRead] = {}
next_id = 1

@app.get("/", tags=["root"])
def home() -> dict[str, str]:
    return {"message": "Hello from FastAPI Cloud"}

@app.get("/health", tags=["health"])
def health() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/items", response_model=ItemRead, status_code=status.HTTP_201_CREATED, tags=["items"])
def create_item(payload: ItemCreate) -> ItemRead:
    global next_id
    item = ItemRead(id=next_id, **payload.model_dump())
    items[next_id] = item
    next_id += 1
    return item

@app.get("/items", response_model=list[ItemRead], tags=["items"])
def list_items(
    limit: Annotated[int, Query(ge=1, le=100)] = 10,
    offset: Annotated[int, Query(ge=0)] = 0,
) -> list[ItemRead]:
    return list(items.values())[offset : offset + limit]

@app.get("/items/{item_id}", response_model=ItemRead, tags=["items"])
def get_item(item_id: Annotated[int, Path(ge=1)]) -> ItemRead:
    item = items.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.patch("/items/{item_id}", response_model=ItemRead, tags=["items"])
def update_item(item_id: Annotated[int, Path(ge=1)], payload: ItemUpdate) -> ItemRead:
    item = items.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    update_data = payload.model_dump(exclude_unset=True)
    updated = item.model_copy(update=update_data)
    items[item_id] = updated
    return updated

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["items"])
def delete_item(item_id: Annotated[int, Path(ge=1)]) -> None:
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
```

Важно: это учебный код. Он специально хранит данные в памяти, чтобы не отвлекаться на базу.

## 38. Краткая шпаргалка синтаксиса

```python
# Импорт приложения
from fastapi import FastAPI

# Создание приложения
app = FastAPI()

# GET endpoint
@app.get("/")
def home():
    return {"message": "Hello"}

# Path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# Query parameter
@app.get("/items")
def read_items(limit: int = 10):
    return {"limit": limit}

# Body через Pydantic
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

@app.post("/items")
def create_item(item: Item):
    return item

# Ошибка
from fastapi import HTTPException

raise HTTPException(status_code=404, detail="Not found")

# Dependency
from typing import Annotated
from fastapi import Depends

def get_user():
    return {"name": "demo"}

@app.get("/me")
def me(user: Annotated[dict, Depends(get_user)]):
    return user
```

## 39. Лучшие привычки с самого начала

- Пиши типы у параметров и возвращаемых значений.
- Используй `response_model` для публичных ответов.
- Разделяй модели входа и выхода.
- Не храни секреты в коде.
- Не возвращай внутренние поля.
- Используй `HTTPException` для ожидаемых ошибок.
- Используй `status.HTTP_...`, а не голые числа, когда код не очевиден.
- Проверяй `/docs` после каждого изменения.
- Пиши маленькие endpoints.
- Не усложняй архитектуру раньше времени.
- Сначала добейся ясности, потом красоты.

## 40. Главная мысль

FastAPI учится не через запоминание всех декораторов, а через понимание потока:

```text
HTTP request
-> route match
-> parameter parsing
-> Pydantic validation
-> dependencies
-> endpoint function
-> response_model filtering
-> JSON response
-> OpenAPI documentation
```

Если ты понимаешь этот поток, почти весь FastAPI становится предсказуемым.

## 41. Python-минимум, без которого FastAPI будет казаться магией

FastAPI очень сильно опирается на обычный Python. Если эти основы неясны, декораторы, типы и Pydantic будут выглядеть загадочно.

### Переменная

```python
message = "Hello"
```

`message` - имя. `"Hello"` - значение.

В FastAPI:

```python
app = FastAPI()
```

`app` - переменная, которая хранит объект приложения.

### Функция

```python
def hello() -> str:
    return "Hello"
```

Разбор:

- `def` - define, "определить".
- `hello` - имя функции.
- `()` - место для параметров.
- `-> str` - обещание/подсказка, что функция возвращает строку.
- `return` - вернуть результат.

В FastAPI endpoint - это обычная функция:

```python
@app.get("/")
def home() -> dict[str, str]:
    return {"message": "Hello"}
```

FastAPI вызывает эту функцию, когда приходит подходящий HTTP-запрос.

### Класс

```python
class User:
    pass
```

`class` описывает тип объектов. В FastAPI классы часто нужны для Pydantic-схем:

```python
from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str
```

Почему `UserCreate` с большой буквы:

- это класс;
- классы в Python принято писать в `PascalCase`;
- `UserCreate` читается как "модель данных для создания пользователя".

### Импорт

```python
from fastapi import FastAPI
```

Это значит: из пакета `fastapi` взять имя `FastAPI`.

```python
from fastapi import FastAPI, HTTPException, status
```

Так импортируют несколько имен сразу.

### Словарь

```python
data = {"message": "Hello"}
```

Словарь - пары ключ/значение.

FastAPI часто возвращает словари:

```python
return {"status": "ok"}
```

FastAPI превратит это в JSON:

```json
{
  "status": "ok"
}
```

### Список

```python
users = ["Anna", "Bohdan", "Ira"]
```

В API список часто означает "много объектов":

```python
@app.get("/users")
def list_users() -> list[str]:
    return ["Anna", "Bohdan", "Ira"]
```

### `None`

`None` значит "значения нет".

```python
q: str | None = None
```

Это читается так:

- `q` может быть строкой;
- или может быть `None`;
- по умолчанию `None`.

В query-параметрах это значит: параметр необязательный.

## 42. Как читать endpoint как предложение

Возьмем код:

```python
@app.get("/items/{item_id}", response_model=ItemRead, tags=["items"])
def get_item(item_id: int) -> ItemRead:
    ...
```

Читай его так:

```text
Когда клиент отправляет GET-запрос на /items/{item_id},
FastAPI должен вызвать функцию get_item.
Параметр item_id нужно взять из пути и привести к int.
Ответ нужно проверить и показать наружу как ItemRead.
В документации endpoint должен попасть в группу items.
```

Такой способ чтения снимает большую часть сложности.

Еще пример:

```python
@app.post("/users", response_model=UserPublic, status_code=201, tags=["users"])
def create_user(payload: UserCreate) -> UserPublic:
    ...
```

Читаем:

```text
POST /users создает пользователя.
Тело запроса должно соответствовать UserCreate.
Ответ наружу должен соответствовать UserPublic.
При успехе вернется HTTP 201 Created.
В документации это будет в разделе users.
```

## 43. Декоратор `@app.get` максимально простыми словами

Декоратор - это строка над функцией, которая что-то делает с функцией.

```python
@app.get("/")
def home():
    return {"message": "Hello"}
```

FastAPI не вызывает `home()` сразу. Он регистрирует функцию в таблице маршрутов.

Упрощенно внутри FastAPI появляется такая запись:

```text
GET / -> home
```

Когда приходит запрос:

```text
GET /
```

FastAPI ищет совпадение и вызывает `home`.

Почему используется декоратор:

- код маршрута находится прямо рядом с функцией;
- легко видеть, какой URL связан с какой функцией;
- Python-декораторы хорошо подходят для регистрации.

Можно представить без магии:

```python
def home():
    return {"message": "Hello"}

app.get("/")(home)
```

Запись с `@` - просто более удобная форма.

## 44. Type hints: почему FastAPI так любит типы

Type hints - подсказки типов.

```python
def add(a: int, b: int) -> int:
    return a + b
```

Python сам по себе не запрещает передать строку, но FastAPI использует эти подсказки для API.

```python
@app.get("/double/{number}")
def double(number: int) -> dict[str, int]:
    return {"result": number * 2}
```

Если клиент откроет:

```text
/double/10
```

FastAPI:

- увидит `number: int`;
- возьмет `"10"` из URL;
- превратит в `10`;
- передаст в функцию как число.

Если клиент откроет:

```text
/double/abc
```

FastAPI:

- попробует превратить `"abc"` в `int`;
- не сможет;
- вернет ошибку валидации.

Типы дают сразу четыре преимущества:

- автодополнение в редакторе;
- проверка данных;
- документация;
- меньше ручного кода.

## 45. Как читать ошибку `422`

Одна из самых частых ошибок новичка:

```json
{
  "detail": [
    {
      "type": "int_parsing",
      "loc": ["path", "item_id"],
      "msg": "Input should be a valid integer, unable to parse string as an integer",
      "input": "abc"
    }
  ]
}
```

Разбор:

- `detail` - список деталей ошибки.
- `type` - тип ошибки.
- `loc` - location, место ошибки.
- `["path", "item_id"]` значит: ошибка в path-параметре `item_id`.
- `msg` - human-readable сообщение.
- `input` - что реально пришло от клиента.

Алгоритм чтения:

1. Смотри на `loc`.
2. Смотри на `msg`.
3. Смотри на `input`.
4. Сравни с типом в функции или Pydantic-модели.

Пример ошибки body:

```json
{
  "detail": [
    {
      "type": "missing",
      "loc": ["body", "email"],
      "msg": "Field required",
      "input": {"password": "secret"}
    }
  ]
}
```

Это значит:

- ошибка в теле запроса;
- не хватает поля `email`;
- клиент прислал только `password`.

## 46. Как проектировать endpoint правильно

Плохое API часто начинается с плохого URL.

### Думай ресурсами

Ресурс - объект предметной области:

- пользователь;
- товар;
- заказ;
- заметка;
- комментарий;
- файл.

Хорошо:

```text
GET /users
POST /users
GET /users/{user_id}
PATCH /users/{user_id}
DELETE /users/{user_id}
```

Плохо:

```text
GET /get-users
POST /create-user
POST /delete-user
GET /update-user
```

Почему плохо:

- действие уже есть в HTTP-методе;
- `GET /update-user` звучит как чтение, но делает изменение;
- frontend и другие разработчики будут путаться.

### Таблица REST-мышления

| Что нужно | Метод | Путь | Тело |
|---|---|---|---|
| Получить список | `GET` | `/notes` | нет |
| Получить одну запись | `GET` | `/notes/{note_id}` | нет |
| Создать | `POST` | `/notes` | JSON с данными |
| Обновить частично | `PATCH` | `/notes/{note_id}` | JSON с частью полей |
| Заменить целиком | `PUT` | `/notes/{note_id}` | полный JSON |
| Удалить | `DELETE` | `/notes/{note_id}` | обычно нет |

### Когда использовать глагол в пути

Иногда действие не является обычным CRUD.

Допустимо:

```text
POST /auth/login
POST /auth/logout
POST /orders/{order_id}/cancel
POST /users/{user_id}/reset-password
```

Почему `POST`:

- происходит действие;
- оно меняет состояние;
- это не просто чтение ресурса.

## 47. OpenAPI: что FastAPI генерирует за тебя

OpenAPI - стандарт описания API.

FastAPI строит OpenAPI-схему из:

- путей;
- методов;
- параметров;
- Pydantic-моделей;
- status codes;
- response models;
- tags;
- descriptions.

Открой:

```text
http://127.0.0.1:8000/openapi.json
```

Ты увидишь JSON со схемой API.

Swagger UI на `/docs` читает этот JSON и строит красивый интерфейс.

ReDoc на `/redoc` тоже читает этот JSON, но показывает иначе.

Почему это мощно:

- frontend может видеть точный контракт;
- можно генерировать клиентов;
- можно проверять API автоматически;
- документация не отстает от кода, если ты правильно пишешь типы.

### Полезные параметры декоратора

```python
@app.get(
    "/items/{item_id}",
    response_model=ItemRead,
    tags=["items"],
    summary="Get item",
    description="Return one item by its unique identifier.",
    response_description="The requested item.",
)
def get_item(item_id: int) -> ItemRead:
    ...
```

Что значит:

- `summary` - короткий заголовок операции.
- `description` - подробное описание.
- `response_description` - описание успешного ответа.
- `tags` - группировка в документации.

Не нужно писать огромные описания для очевидных endpoints. Лучше хорошие имена, типы и модели.

## 48. Как проверять API руками

### Через браузер

Браузер удобен для `GET`:

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/items/1
http://127.0.0.1:8000/items?limit=10&offset=0
```

Но браузер неудобен для `POST`, `PATCH`, `DELETE`.

### Через `/docs`

`/docs` - лучший инструмент новичка:

1. Открой endpoint.
2. Нажми "Try it out".
3. Введи параметры.
4. Нажми "Execute".
5. Посмотри request URL, response body и status code.

Обязательно смотри не только JSON, но и status code.

### Через `curl`

`curl` - командный HTTP-клиент.

GET:

```bash
curl http://127.0.0.1:8000/
```

POST JSON:

```bash
curl -X POST http://127.0.0.1:8000/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Keyboard", "price": 99.9}'
```

Разбор:

- `-X POST` задает HTTP-метод.
- `-H` добавляет header.
- `Content-Type: application/json` говорит серверу, что тело - JSON.
- `-d` передает body.

PATCH:

```bash
curl -X PATCH http://127.0.0.1:8000/items/1 \
  -H "Content-Type: application/json" \
  -d '{"price": 79.9}'
```

DELETE:

```bash
curl -X DELETE http://127.0.0.1:8000/items/1
```

## 49. Ответы: не только словари

Чаще всего в FastAPI возвращают:

```python
return {"status": "ok"}
```

Но можно возвращать разные типы.

### Список

```python
@app.get("/numbers")
def numbers() -> list[int]:
    return [1, 2, 3]
```

### Pydantic-модель

```python
@app.get("/item", response_model=ItemRead)
def get_item() -> ItemRead:
    return ItemRead(id=1, name="Keyboard", price=99.9)
```

### Response напрямую

```python
from fastapi import Response

@app.get("/empty")
def empty() -> Response:
    return Response(status_code=204)
```

### JSONResponse

```python
from fastapi.responses import JSONResponse

@app.get("/custom")
def custom_response() -> JSONResponse:
    return JSONResponse(
        status_code=202,
        content={"status": "accepted"},
    )
```

Когда использовать обычный `return dict`:

- почти всегда для JSON API.

Когда использовать `JSONResponse`:

- нужно вручную задать status code;
- нужно вручную задать headers;
- нужен нестандартный ответ.

## 50. `PUT` и `PATCH`: разница на примере

Есть объект:

```json
{
  "id": 1,
  "name": "Keyboard",
  "price": 99.9,
  "description": "Mechanical"
}
```

### `PUT`

`PUT` обычно означает полную замену.

Запрос:

```json
{
  "name": "Mouse",
  "price": 49.9,
  "description": null
}
```

После `PUT` объект полностью становится таким, как прислал клиент.

### `PATCH`

`PATCH` означает частичное обновление.

Запрос:

```json
{
  "price": 79.9
}
```

После `PATCH` меняется только `price`, остальные поля остаются.

В Pydantic v2 для `PATCH` часто используют:

```python
update_data = payload.model_dump(exclude_unset=True)
```

Почему `exclude_unset=True`:

- `unset` - не установленное;
- если клиент не передал поле, мы его не трогаем;
- если клиент явно передал `null`, это уже осознанное значение.

## 51. Пагинация, фильтрация, сортировка

Когда endpoint возвращает список, почти всегда нужны ограничения.

Плохо:

```python
@app.get("/users")
def list_users() -> list[UserRead]:
    return all_users
```

Если пользователей миллион, сервер и клиенту будет плохо.

Лучше:

```python
from typing import Annotated
from fastapi import Query

@app.get("/users")
def list_users(
    limit: Annotated[int, Query(ge=1, le=100)] = 20,
    offset: Annotated[int, Query(ge=0)] = 0,
    q: Annotated[str | None, Query(max_length=100)] = None,
) -> list[UserRead]:
    ...
```

Смысл:

- `limit` - максимум записей;
- `offset` - сколько пропустить;
- `q` - поисковая строка.

Сортировка:

```python
from enum import StrEnum

class UserSort(StrEnum):
    created_at = "created_at"
    email = "email"

@app.get("/users")
def list_users(sort_by: UserSort = UserSort.created_at):
    ...
```

Почему `StrEnum`:

- клиент может выбрать только разрешенные значения;
- `/docs` покажет выпадающий список;
- меньше ошибок в строках.

## 52. Enums: ограниченный набор значений

Enum - перечисление.

```python
from enum import StrEnum

class OrderStatus(StrEnum):
    pending = "pending"
    paid = "paid"
    shipped = "shipped"
    cancelled = "cancelled"
```

Endpoint:

```python
@app.get("/orders")
def list_orders(status: OrderStatus | None = None):
    return {"status": status}
```

Плюсы:

- нельзя случайно передать `shiped` вместо `shipped`;
- OpenAPI покажет допустимые значения;
- код сам документирует бизнес-правила.

Почему значения часто lowercase:

- URL и JSON обычно пишут в нижнем регистре;
- легче читать;
- меньше проблем с регистром.

## 53. Alias: когда имя в JSON отличается от имени в Python

В Python принято:

```python
first_name: str
```

В некоторых API принято:

```json
{
  "firstName": "Anna"
}
```

Это называется `camelCase`.

Pydantic умеет alias:

```python
from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    first_name: str = Field(alias="firstName")
```

Но новичку лучше сначала использовать один стиль:

- Python-код: `snake_case`;
- JSON API: тоже можно `snake_case`, если ты контролируешь API;
- если frontend требует `camelCase`, изучай alias отдельно.

## 54. Валидация бизнес-правил

Pydantic проверяет форму данных:

- тип;
- длину;
- обязательность;
- диапазон.

Но бизнес-правила часто нужно проверять самому.

Пример:

```python
@app.post("/users")
def create_user(payload: UserCreate) -> UserPublic:
    if payload.email in existing_emails:
        raise HTTPException(status_code=409, detail="Email already exists")
    ...
```

Почему `409 Conflict`:

- запрос понятен;
- данные валидны;
- но текущее состояние системы конфликтует с действием;
- email уже занят.

Другие бизнес-ошибки:

- нельзя отменить уже доставленный заказ;
- нельзя удалить пользователя с активными платежами;
- нельзя создать бронь на занятое время.

## 55. Слои приложения: endpoint, service, repository

Когда проект растет, код лучше разделять.

### Endpoint layer

Отвечает за HTTP:

- принять параметры;
- вызвать service;
- вернуть response model;
- выбросить HTTP-ошибку при необходимости.

```python
@router.post("/users", response_model=UserPublic)
def create_user(payload: UserCreate, service: UserServiceDep) -> UserPublic:
    return service.create_user(payload)
```

### Service layer

Отвечает за бизнес-логику:

- проверить правила;
- захэшировать пароль;
- вызвать repository;
- отправить событие.

```python
class UserService:
    def create_user(self, payload: UserCreate) -> UserPublic:
        ...
```

### Repository layer

Отвечает за хранение:

- SQL-запросы;
- ORM;
- чтение/запись в БД.

```python
class UserRepository:
    def get_by_email(self, email: str) -> User | None:
        ...
```

Для маленького учебного проекта это не нужно сразу. Но понимать идею полезно: endpoint не должен превращаться в огромную функцию на 200 строк.

## 56. База данных: учебная дорожная карта

Не начинай с базы в первый день. Порядок лучше такой:

1. CRUD в памяти.
2. Pydantic-модели.
3. Ошибки и status codes.
4. `Depends`.
5. Только потом БД.

### SQLite

SQLite - файл-база данных. Хороша для обучения.

Плюсы:

- не нужен отдельный сервер;
- база лежит в одном файле;
- удобно для первых проектов.

Минусы:

- не всегда подходит для больших production-систем;
- есть особенности параллельной записи.

### PostgreSQL

PostgreSQL - популярная production-БД.

Плюсы:

- надежная;
- мощная;
- хорошо подходит для backend-проектов.

Минусы:

- нужно поднимать сервер;
- больше настроек;
- новичку сложнее стартовать.

### ORM

ORM позволяет писать Python-код вместо ручного SQL для типовых операций.

Но ORM не отменяет SQL. Хороший backend-разработчик постепенно учит оба уровня.

## 57. Миграции: почему нельзя просто менять таблицы руками

Миграция - это версия изменения структуры базы.

Пример:

```text
001_create_users_table
002_add_is_active_to_users
003_create_orders_table
```

Зачем:

- команда видит историю изменений;
- production можно обновлять предсказуемо;
- можно откатить или понять, что поменялось;
- база не расходится с кодом.

В Python часто используют Alembic.

Новичку пока достаточно запомнить:

- Pydantic model - форма данных API;
- ORM model - таблица/объект базы;
- migration - изменение структуры базы.

Это три разные вещи.

## 58. Авторизация глубже: пароль, hash, token

Никогда не храни пароль как обычную строку.

Плохо:

```text
password = "qwerty123"
```

Правильно хранить hash:

```text
hashed_password = "$argon2id$..."
```

Hash - одностороннее преобразование. Сервер не должен уметь восстановить исходный пароль.

Типичный login flow:

```text
1. Пользователь отправляет email и password.
2. Сервер ищет пользователя по email.
3. Сервер проверяет password против hashed_password.
4. Если верно, сервер выдает access token.
5. Клиент отправляет token в Authorization header.
```

Access token:

```http
Authorization: Bearer eyJ...
```

Важные слова:

- `access token` - короткоживущий токен доступа.
- `refresh token` - токен для обновления access token.
- `expiration` - срок жизни токена.
- `scope` - область прав, например `users:read`.
- `claim` - утверждение внутри JWT, например `sub`, `exp`, `iat`.

Почему `sub`:

- subject, субъект токена;
- обычно id пользователя.

Почему `exp`:

- expiration time;
- время истечения токена.

Почему `iat`:

- issued at;
- когда токен был выпущен.

## 59. Testing mindset: что именно тестировать

Тесты API должны проверять поведение, а не внутренности.

Хороший тест:

```python
def test_home() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI Cloud"}
```

Что он проверяет:

- endpoint существует;
- status code правильный;
- JSON правильный.

Тест на ошибку:

```python
def test_item_not_found() -> None:
    response = client.get("/items/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}
```

Тест на валидацию:

```python
def test_item_id_must_be_int() -> None:
    response = client.get("/items/abc")
    assert response.status_code == 422
```

Что тестировать в учебном проекте:

- happy path: все хорошо;
- not found: объект не найден;
- validation error: неверные данные;
- security: без токена нельзя;
- response shape: наружу не ушли лишние поля.

## 60. Debugging: как искать ошибку без паники

Алгоритм:

1. Прочитай traceback снизу вверх.
2. Найди файл своего проекта.
3. Посмотри строку.
4. Определи тип ошибки.
5. Проверь входные данные.
6. Проверь типы.
7. Упрости пример до минимального.

Частые ошибки:

### `ModuleNotFoundError`

```text
ModuleNotFoundError: No module named 'fastapi'
```

Причины:

- не активировано окружение;
- зависимости не установлены;
- команда запущена не из того Python.

### `ImportError`

```text
ImportError: cannot import name ...
```

Причины:

- имя написано неправильно;
- импортируешь не из того модуля;
- циклический импорт.

### `NameError`

```text
NameError: name 'app' is not defined
```

Причины:

- переменная не создана;
- опечатка;
- код идет не в том порядке.

### `TypeError`

```text
TypeError: ...
```

Обычно значит: функция получила не тот тип или не то количество аргументов.

### `ValidationError`

Pydantic говорит: данные не соответствуют модели.

Не злись на Pydantic. Он делает ровно то, что должен: ловит плохие данные на входе.

## 61. Логирование

`print()` полезен в первые дни, но в приложениях используют logging.

```python
import logging

logger = logging.getLogger(__name__)

@app.get("/health")
def health() -> dict[str, str]:
    logger.info("Health check requested")
    return {"status": "ok"}
```

Почему `__name__`:

- это имя текущего Python-модуля;
- лог показывает, откуда пришло сообщение.

Уровни логов:

- `debug` - подробности для разработки;
- `info` - обычные события;
- `warning` - подозрительно, но приложение работает;
- `error` - ошибка операции;
- `critical` - серьезная проблема.

В production логи должны помогать ответить:

- что произошло;
- когда;
- с каким request id;
- для какого пользователя;
- почему упало.

## 62. Request ID

Request ID - уникальный id запроса.

Зачем:

- связать логи одного запроса;
- быстрее искать проблему;
- передать id пользователю при ошибке.

Пример идеи:

```text
Request X-Request-ID: abc-123
Log: abc-123 started GET /items
Log: abc-123 database query
Log: abc-123 completed 200
```

В больших системах это обязательно. В учебном проекте достаточно понимать концепцию.

## 63. Версионирование API

Когда API меняется, старые клиенты могут сломаться.

Один из простых способов:

```text
/api/v1/users
/api/v2/users
```

Почему `v1`:

- `v` - version;
- `1` - первая версия контракта.

Не нужно добавлять `/api/v1` в самый первый учебный endpoint. Но в реальных проектах это частая практика.

Пример router:

```python
router = APIRouter(prefix="/api/v1/users", tags=["users"])
```

## 64. Что значит "контракт API"

Контракт API - договор между backend и клиентом.

Он включает:

- путь;
- метод;
- query/path/body параметры;
- status codes;
- формат успешного ответа;
- формат ошибок;
- правила авторизации.

Если backend внезапно поменял поле:

```json
{"user_id": 1}
```

на:

```json
{"id": 1}
```

frontend может сломаться.

Поэтому:

- меняй API осознанно;
- используй `response_model`;
- документируй изменения;
- пиши тесты на важные ответы.

## 65. Мини-проект для закрепления: Notes API

Цель: сделать API заметок без базы данных.

### Модели

```python
from pydantic import BaseModel, Field

class NoteCreate(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    text: str = Field(min_length=1)

class NoteRead(NoteCreate):
    id: int
    is_done: bool = False

class NoteUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=120)
    text: str | None = Field(default=None, min_length=1)
    is_done: bool | None = None
```

### Endpoints

Нужно реализовать:

```text
POST /notes
GET /notes
GET /notes/{note_id}
PATCH /notes/{note_id}
DELETE /notes/{note_id}
```

### Требования

- `POST /notes` возвращает `201`.
- `GET /notes/{note_id}` возвращает `404`, если заметки нет.
- `PATCH` обновляет только переданные поля.
- `DELETE` возвращает `204`.
- Все endpoints имеют `tags=["notes"]`.
- Все ответы используют `response_model`, где это применимо.

### Самопроверка

После реализации открой `/docs` и проверь:

- модели видны в Schemas;
- поля имеют ограничения;
- `POST` показывает JSON body;
- `PATCH` позволяет отправить часть полей;
- неверный `note_id=abc` дает `422`;
- несуществующий `note_id=999` дает `404`.

## 66. Учебные упражнения по уровням

### Уровень 1: совсем начало

- Измени сообщение в `/`.
- Добавь `/health`.
- Добавь `/version`.
- Верни список строк.
- Верни словарь с несколькими полями.

### Уровень 2: параметры

- Добавь `/hello/{name}`.
- Добавь query `?uppercase=true`.
- Добавь ограничение `name` по длине.
- Проверь ошибку `422`.

### Уровень 3: Pydantic

- Создай `BookCreate`.
- Создай `BookRead`.
- Сделай `POST /books`.
- Сделай `GET /books`.

### Уровень 4: ошибки

- Верни `404`, если книга не найдена.
- Верни `409`, если название уже существует.
- Верни `400`, если операция логически невозможна.

### Уровень 5: архитектура

- Перенеси books routes в `routers/books.py`.
- Добавь `APIRouter`.
- Подключи router в `main.py`.

### Уровень 6: тесты

- Напиши тест для `/health`.
- Напиши тест для создания книги.
- Напиши тест для `404`.
- Напиши тест для `422`.

## 67. Чеклист перед тем, как идти дальше

Ты готов переходить к базе данных, если можешь без подсказки:

- создать `FastAPI()` приложение;
- объяснить `main:app`;
- написать `GET`, `POST`, `PATCH`, `DELETE`;
- объяснить path/query/body;
- создать Pydantic-модель;
- использовать `Field`;
- прочитать ошибку `422`;
- вернуть `HTTPException`;
- объяснить `response_model`;
- сделать простой `Depends`;
- открыть и использовать `/docs`;
- написать хотя бы один тест через `TestClient`.

Если несколько пунктов пока туманные, это нормально. Просто вернись к соответствующей главе и повтори руками.

## 68. Большая карта FastAPI

```text
FastAPI
├── Routing
│   ├── @app.get
│   ├── @app.post
│   ├── APIRouter
│   └── tags
├── Data input
│   ├── Path
│   ├── Query
│   ├── Body
│   ├── Header
│   ├── Cookie
│   ├── Form
│   └── File
├── Validation
│   ├── type hints
│   ├── Pydantic BaseModel
│   ├── Field
│   └── Annotated
├── Output
│   ├── response_model
│   ├── status_code
│   ├── Response
│   └── JSONResponse
├── Errors
│   ├── HTTPException
│   ├── 404
│   ├── 409
│   └── 422
├── Architecture
│   ├── routers
│   ├── dependencies
│   ├── services
│   └── settings
├── Advanced
│   ├── middleware
│   ├── lifespan
│   ├── background tasks
│   └── WebSocket
└── Production
    ├── tests
    ├── database
    ├── auth
    ├── logging
    ├── CORS
    └── deployment
```

Эта карта помогает не теряться. FastAPI большой, но он состоит из понятных блоков.

## 69. Как вести свой конспект

Лучший конспект - не копия документации, а твои собственные объяснения.

Для каждой темы записывай:

```text
Тема:
Что это:
Зачем нужно:
Минимальный пример:
Типичная ошибка:
Как проверить:
```

Пример:

```text
Тема: Query parameter
Что это: параметр после ? в URL.
Зачем нужно: фильтрация, поиск, пагинация.
Минимальный пример: /items?limit=10
Типичная ошибка: думать, что query идет из body.
Как проверить: открыть /docs и отправить запрос.
```

Такой конспект быстро превращается в личную базу знаний.

## 70. Финальная учебная стратегия

FastAPI лучше всего изучать спиралью:

```text
маленький endpoint
-> Pydantic-модель
-> ошибка
-> документация
-> тест
-> маленький рефакторинг
-> повторить
```

Не нужно ждать, пока ты "выучишь весь FastAPI", чтобы писать код. Пиши маленькие работающие куски и каждый раз добавляй один новый инструмент.

Главный ориентир новичка:

- endpoint должен быть понятен;
- данные должны быть валидированы;
- ошибки должны быть честными;
- ответ должен быть предсказуемым;
- документация должна совпадать с кодом.

Если это выполняется, ты уже пишешь хороший FastAPI-код.

## 71. Query Parameter Models

Официальная документация FastAPI отдельно показывает **Query Parameter Models**. Идея простая: если query-параметров много, их можно собрать в Pydantic-модель.

Обычный вариант:

```python
from typing import Annotated
from fastapi import Query

@app.get("/items")
def list_items(
    limit: Annotated[int, Query(ge=1, le=100)] = 20,
    offset: Annotated[int, Query(ge=0)] = 0,
    order_by: str = "created_at",
) -> dict[str, int | str]:
    return {"limit": limit, "offset": offset, "order_by": order_by}
```

Когда параметров становится много, сигнатура функции разрастается.

Вариант с моделью:

```python
from typing import Annotated, Literal

from fastapi import Query
from pydantic import BaseModel, Field

class PaginationParams(BaseModel):
    limit: int = Field(default=20, ge=1, le=100)
    offset: int = Field(default=0, ge=0)
    order_by: Literal["created_at", "name", "price"] = "created_at"

@app.get("/items")
def list_items(
    params: Annotated[PaginationParams, Query()]
) -> PaginationParams:
    return params
```

Почему это полезно:

- параметры можно переиспользовать;
- endpoint становится короче;
- ограничения живут рядом;
- модель видна в документации.

Почему `Literal`:

- literal - "буквальное значение";
- клиент может передать только одно из перечисленных значений;
- это удобно для сортировки, фильтров и режимов.

Когда использовать:

- фильтры каталога;
- пагинация;
- сортировка;
- поисковые параметры;
- repeated query groups.

Когда не использовать:

- если параметра всего два;
- если модель усложняет чтение;
- если ты еще только учишься path/query/body.

## 72. Body - Multiple Parameters

Официальная документация показывает, что endpoint может принимать одновременно:

- path parameters;
- query parameters;
- body model;
- несколько body-параметров.

Пример:

```python
from typing import Annotated

from fastapi import Body
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float

class User(BaseModel):
    username: str

@app.put("/items/{item_id}")
def update_item(
    item_id: int,
    item: Item,
    user: User,
    importance: Annotated[int, Body(gt=0)],
) -> dict:
    return {
        "item_id": item_id,
        "item": item,
        "user": user,
        "importance": importance,
    }
```

Тело запроса будет таким:

```json
{
  "item": {
    "name": "Keyboard",
    "price": 99.9
  },
  "user": {
    "username": "anna"
  },
  "importance": 5
}
```

Почему body стал объектом с ключами `item`, `user`, `importance`:

- body-параметров несколько;
- FastAPI должен понять, какое значение какому параметру соответствует;
- поэтому каждый параметр получает свой ключ.

### `embed=True`

Если body-параметр один, FastAPI обычно ожидает сам объект:

```json
{
  "name": "Keyboard",
  "price": 99.9
}
```

Но можно заставить ожидать ключ:

```python
from typing import Annotated
from fastapi import Body

@app.post("/items")
def create_item(item: Annotated[Item, Body(embed=True)]) -> Item:
    return item
```

Тогда body:

```json
{
  "item": {
    "name": "Keyboard",
    "price": 99.9
  }
}
```

Для новичка правило простое: обычно не нужен `embed=True`, пока API-контракт явно этого не требует.

## 73. Nested Models и Extra Data Types

### Вложенные модели

Вложенная модель - это модель внутри модели.

```python
from pydantic import BaseModel, Field

class Image(BaseModel):
    url: str
    name: str

class Item(BaseModel):
    name: str
    price: float = Field(gt=0)
    images: list[Image] = []
```

JSON:

```json
{
  "name": "Phone",
  "price": 799.0,
  "images": [
    {
      "url": "https://example.com/phone.png",
      "name": "front"
    }
  ]
}
```

Почему это удобно:

- сложные JSON-структуры описываются Python-классами;
- FastAPI документирует вложенность;
- ошибки показывают точное место.

Ошибка может выглядеть так:

```json
{
  "loc": ["body", "images", 0, "url"],
  "msg": "Field required"
}
```

Это значит: в body, в списке `images`, у первого элемента нет поля `url`.

### Extra Data Types

FastAPI через Pydantic поддерживает не только `str`, `int`, `float`, `bool`.

Частые типы:

```python
from datetime import date, datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, EmailStr

class UserEvent(BaseModel):
    id: UUID
    email: EmailStr
    created_at: datetime
    birthday: date | None = None
    amount: Decimal
```

Что это дает:

- `UUID` проверяет формат уникального id;
- `EmailStr` проверяет email;
- `datetime` проверяет дату и время;
- `date` проверяет дату без времени;
- `Decimal` лучше для денег, чем `float`.

Почему `float` плох для денег:

- числа с плавающей точкой могут иметь погрешность;
- для денег лучше `Decimal`;
- в базе данных тоже обычно используют decimal/numeric типы.

## 74. Header/Cookie Parameter Models и underscore conversion

Официальная документация показывает не только отдельные `Header()` и `Cookie()`, но и модели параметров.

### Header underscore conversion

HTTP-header часто выглядит так:

```http
User-Agent: Mozilla/5.0
X-Request-ID: abc-123
```

В Python нельзя удобно писать переменную с дефисом:

```python
user-agent = "bad"
```

Это будет синтаксическая ошибка, потому что `-` означает минус.

Поэтому в Python пишут:

```python
from typing import Annotated
from fastapi import Header

@app.get("/headers")
def read_headers(
    user_agent: Annotated[str | None, Header()] = None,
    x_request_id: Annotated[str | None, Header()] = None,
) -> dict[str, str | None]:
    return {"user_agent": user_agent, "x_request_id": x_request_id}
```

FastAPI автоматически сопоставляет:

- `user_agent` -> `user-agent`;
- `x_request_id` -> `x-request-id`.

Это называется underscore conversion.

### Cookie model

```python
from typing import Annotated

from fastapi import Cookie
from pydantic import BaseModel

class CookieParams(BaseModel):
    session_id: str
    theme: str | None = None

@app.get("/cookie-info")
def cookie_info(cookies: Annotated[CookieParams, Cookie()]) -> CookieParams:
    return cookies
```

Для новичка важно: cookies и headers - это не body и не query. Это отдельные части HTTP-запроса.

## 75. Request Forms and Files

JSON - не единственный формат запроса.

### Login form

OAuth2 password flow в документации использует form-data:

```python
from typing import Annotated
from fastapi import Form

@app.post("/login")
def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
) -> dict[str, str]:
    return {"username": username}
```

Почему не JSON:

- OAuth2 password flow исторически использует form fields;
- HTML-формы тоже отправляют form-data;
- FastAPI явно отделяет `Form()` от JSON body.

### File + Form

```python
from typing import Annotated
from fastapi import File, Form, UploadFile

@app.post("/profile")
def update_profile(
    display_name: Annotated[str, Form()],
    avatar: Annotated[UploadFile, File()],
) -> dict[str, str]:
    return {
        "display_name": display_name,
        "filename": avatar.filename,
    }
```

Тут запрос будет `multipart/form-data`, потому что в нем есть файл.

Когда использовать:

- загрузка аватара;
- импорт CSV;
- загрузка документов;
- форма с текстом и файлом одновременно.

## 76. Path Operation Configuration и Metadata

Официальная документация показывает много настроек path operation.

```python
@app.get(
    "/items/{item_id}",
    tags=["items"],
    summary="Read one item",
    description="Return one item by ID. Raises 404 if the item does not exist.",
    response_description="The requested item.",
    deprecated=False,
)
def read_item(item_id: int) -> ItemRead:
    ...
```

Разбор:

- `tags` группирует endpoints.
- `summary` коротко описывает операцию.
- `description` объясняет подробнее.
- `response_description` описывает успешный ответ.
- `deprecated=True` помечает endpoint как устаревший.

Почему `deprecated`:

- deprecated - "устаревший, не рекомендуется";
- endpoint еще работает;
- но новых клиентов лучше переводить на другой.

### Metadata приложения

```python
app = FastAPI(
    title="FastAPI Learning",
    summary="Учебное API",
    description="Проект для пошагового изучения FastAPI.",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)
```

Что можно менять:

- `docs_url=None` отключит Swagger UI;
- `redoc_url=None` отключит ReDoc;
- `openapi_url=None` отключит OpenAPI schema и docs.

Для обучения лучше ничего не отключать. `/docs` - твой главный тренажер.

## 77. JSON Compatible Encoder

Официальная документация FastAPI показывает `jsonable_encoder`.

Проблема: не все Python-объекты напрямую являются JSON.

Например:

```python
from datetime import datetime

data = {"created_at": datetime.now()}
```

`datetime` - Python-объект. В JSON нет типа datetime. Его нужно превратить в строку.

FastAPI часто делает это автоматически в ответах. Но если ты сам сохраняешь данные, например в файл, cache или NoSQL-хранилище, может понадобиться:

```python
from datetime import datetime

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

class Event(BaseModel):
    name: str
    created_at: datetime

event = Event(name="startup", created_at=datetime.now())
json_data = jsonable_encoder(event)
```

`json_data` будет состоять из JSON-compatible типов:

- `dict`;
- `list`;
- `str`;
- `int`;
- `float`;
- `bool`;
- `None`.

Запомни: `jsonable_encoder` не обязательно превращает в JSON-строку. Он превращает в данные, которые можно безопасно сериализовать в JSON.

## 78. Dependencies: official-глубина

Официальная документация делит dependencies на несколько тем.

### Простая dependency

```python
from typing import Annotated
from fastapi import Depends

def common_parameters(q: str | None = None, limit: int = 10) -> dict[str, str | int | None]:
    return {"q": q, "limit": limit}

@app.get("/items")
def read_items(
    commons: Annotated[dict[str, str | int | None], Depends(common_parameters)]
) -> dict[str, str | int | None]:
    return commons
```

### Sub-dependency

Dependency может зависеть от другой dependency.

```python
def get_token_header(x_token: str) -> str:
    return x_token

def get_current_user(token: Annotated[str, Depends(get_token_header)]) -> dict[str, str]:
    return {"token": token}
```

FastAPI сам построит цепочку вызовов.

### Dependency в декораторе

Иногда dependency нужна только ради проверки, а результат не нужен в функции.

```python
from fastapi import Depends

def verify_token() -> None:
    ...

@app.get("/private", dependencies=[Depends(verify_token)])
def private() -> dict[str, str]:
    return {"status": "ok"}
```

Почему так:

- endpoint остается чистым;
- dependency выполняется;
- но параметр в функцию не добавляется.

### Global dependencies

```python
app = FastAPI(dependencies=[Depends(verify_token)])
```

Такая dependency применяется ко всем endpoints приложения.

Для новичка осторожно: global dependencies легко забыть и потом удивляться, почему все endpoints требуют токен.

### Classes as dependencies

```python
class CommonQueryParams:
    def __init__(self, q: str | None = None, limit: int = 10):
        self.q = q
        self.limit = limit

@app.get("/items")
def read_items(commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):
    return {"q": commons.q, "limit": commons.limit}
```

Класс удобен, когда dependency имеет состояние или несколько связанных параметров.

## 79. Security по официальной логике

Официальный tutorial идет постепенно:

1. Security - First Steps.
2. Get Current User.
3. Simple OAuth2 with Password and Bearer.
4. OAuth2 with Password, hashing, Bearer with JWT.

Новичку важно не прыгать сразу в JWT.

### Шаг 1: схема токена

```python
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
```

Почему `tokenUrl="token"`:

- это URL, куда клиент должен отправить username/password, чтобы получить token;
- Swagger UI использует это для кнопки Authorize;
- значение относительное, поэтому endpoint будет `/token`.

### Шаг 2: получить token из header

```python
from typing import Annotated
from fastapi import Depends

@app.get("/me")
def read_me(token: Annotated[str, Depends(oauth2_scheme)]) -> dict[str, str]:
    return {"token": token}
```

FastAPI ожидает header:

```http
Authorization: Bearer something
```

### Шаг 3: current user

```python
def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> dict[str, str]:
    return {"username": "demo", "token": token}

@app.get("/users/me")
def read_users_me(
    current_user: Annotated[dict[str, str], Depends(get_current_user)]
) -> dict[str, str]:
    return current_user
```

### Шаг 4: реальная безопасность

Для настоящего проекта нужны:

- password hashing;
- секретный ключ;
- срок жизни токена;
- проверка подписи JWT;
- обработка истекшего токена;
- роли или scopes;
- HTTPS.

Главное правило: security-код нельзя писать "примерно". Его нужно брать из официальной документации, понимать каждую строку и адаптировать осторожно.

## 80. Static Files

FastAPI может отдавать статические файлы: изображения, CSS, JavaScript.

```python
from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="static"), name="static")
```

Структура:

```text
FASTAPI/
├── main.py
└── static/
    ├── logo.png
    └── style.css
```

После этого файл:

```text
static/logo.png
```

будет доступен по:

```text
http://127.0.0.1:8000/static/logo.png
```

Почему `mount`, а не `include_router`:

- `include_router` добавляет API routes в OpenAPI;
- `mount` подключает отдельное ASGI-приложение по префиксу;
- static files не являются API endpoints в обычном смысле.

Для backend API статические файлы часто не нужны, если frontend живет отдельно. Но для простых проектов, админок, демо и документации это полезно.

## Источники для актуализации

Проверено и актуализировано по официальным источникам на **15 мая 2026**.

- FastAPI documentation: https://fastapi.tiangolo.com/
- FastAPI Tutorial - User Guide: https://fastapi.tiangolo.com/tutorial/
- FastAPI First Steps: https://fastapi.tiangolo.com/tutorial/first-steps/
- FastAPI Path Parameters: https://fastapi.tiangolo.com/tutorial/path-params/
- FastAPI Query Parameters: https://fastapi.tiangolo.com/tutorial/query-params/
- FastAPI Request Body: https://fastapi.tiangolo.com/tutorial/body/
- FastAPI Query Parameter Models: https://fastapi.tiangolo.com/tutorial/query-param-models/
- FastAPI Response Model: https://fastapi.tiangolo.com/tutorial/response-model/
- FastAPI Dependencies: https://fastapi.tiangolo.com/tutorial/dependencies/
- FastAPI Security: https://fastapi.tiangolo.com/tutorial/security/
- FastAPI SQL Databases: https://fastapi.tiangolo.com/tutorial/sql-databases/
- FastAPI Bigger Applications: https://fastapi.tiangolo.com/tutorial/bigger-applications/
- FastAPI Testing: https://fastapi.tiangolo.com/tutorial/testing/
- FastAPI Advanced User Guide: https://fastapi.tiangolo.com/advanced/
- FastAPI CLI: https://fastapi.tiangolo.com/fastapi-cli/
- FastAPI release notes: https://fastapi.tiangolo.com/release-notes/
- FastAPI on PyPI: https://pypi.org/project/fastapi/
- Pydantic documentation: https://docs.pydantic.dev/
- Pydantic on PyPI: https://pypi.org/project/pydantic/
- Starlette documentation: https://www.starlette.io/
- Uvicorn documentation: https://www.uvicorn.org/
- OpenAPI specification: https://spec.openapis.org/oas/latest.html
