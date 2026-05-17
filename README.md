# FastAPI Learning

Учебный проект для пошагового изучения **FastAPI** с нуля. Главный материал проекта - подробный русскоязычный учебник [GUIDE.md](GUIDE.md), основанный на официальной документации FastAPI.

Актуально на **15 мая 2026**:

- Python: `>=3.12`
- FastAPI: `0.136.1`
- Pydantic: `2.13.3`
- Starlette: `1.0.0`
- Uvicorn: `0.46.0`
- Точка входа FastAPI: `main:app`

## Что внутри

```text
FASTAPI/
├── main.py          # учебное FastAPI-приложение
├── tests/           # автоматические тесты
├── GUIDE.md         # большой учебник для новичка
├── EXERCISES.md     # практические задания
├── README.md        # эта карта проекта
├── pyproject.toml   # зависимости и настройки проекта
├── uv.lock          # точные версии зависимостей
└── .venv/           # локальное виртуальное окружение, не коммитится
```

## Быстрый старт

Установить зависимости из `uv.lock`:

```bash
uv sync
```

Проверить версии установленных библиотек:

```bash
.venv/bin/python -c "import fastapi, pydantic, starlette, uvicorn; print(fastapi.__version__, pydantic.__version__, starlette.__version__, uvicorn.__version__)"
```

Запустить приложение через FastAPI CLI:

```bash
uv run fastapi dev
```

Альтернативный запуск через Uvicorn:

```bash
uv run uvicorn main:app --reload
```

После запуска открыть:

- `http://127.0.0.1:8000/` - текущий endpoint проекта;
- `http://127.0.0.1:8000/health` - проверка, что приложение работает;
- `http://127.0.0.1:8000/items/5?q=somequery` - учебный path + query пример;
- `http://127.0.0.1:8000/docs` - интерактивная Swagger UI документация;
- `http://127.0.0.1:8000/redoc` - альтернативная ReDoc документация;
- `http://127.0.0.1:8000/openapi.json` - OpenAPI-схема.

Запустить тесты:

```bash
uv run pytest
```

## Как учиться

1. Открой [GUIDE.md](GUIDE.md).
2. Прочитай разделы "Назначение этого гайда", "Как пользоваться этим учебником" и "Строгая структура учебника".
3. Запусти приложение.
4. Повторяй примеры руками в `main.py`.
5. После каждого изменения проверяй результат в `/docs`.
6. Закрепляй темы через [EXERCISES.md](EXERCISES.md).
7. Когда тема понятна, переходи к мини-проекту Notes API.

## Главная идея проекта

Этот репозиторий не про готовый production-backend. Это учебная лаборатория:

- понять HTTP, API, path/query/body;
- изучить FastAPI через официальную документацию;
- освоить Pydantic v2;
- научиться читать ошибки `422`;
- понять `Depends`, `APIRouter`, `response_model`, `status_code`;
- постепенно перейти к тестам, базе данных, авторизации и структуре большого приложения.

## Официальные источники

Учебник сверяется с официальными источниками:

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [FastAPI Tutorial - User Guide](https://fastapi.tiangolo.com/tutorial/)
- [FastAPI Advanced User Guide](https://fastapi.tiangolo.com/advanced/)
- [FastAPI CLI](https://fastapi.tiangolo.com/fastapi-cli/)
- [FastAPI on PyPI](https://pypi.org/project/fastapi/)
- [Pydantic Documentation](https://docs.pydantic.dev/)

## Текущий статус аудита

Сильные стороны:

- проект минимальный и не отвлекает от обучения;
- зависимости актуальны и зафиксированы в `uv.lock`;
- `GUIDE.md` уже покрывает базовые и продвинутые темы FastAPI;
- учебник содержит карту соответствия с официальной документацией.

Следующие учебные этапы:

- добавить пример учебного CRUD API;
- постепенно вынести маршруты в `APIRouter`;
- добавить ответы и подсказки к заданиям;
- добавить CI-проверку Markdown и Python-кода.
