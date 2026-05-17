# FastAPI Exercises

Практические задания к [GUIDE.md](GUIDE.md). Делай их руками в `main.py`, запускай приложение и проверяй результат в `/docs`.

## Как выполнять задания

1. Прочитай тему в `GUIDE.md`.
2. Напиши код сам, не копируя бездумно.
3. Запусти приложение:

```bash
uv run fastapi dev
```

4. Открой `http://127.0.0.1:8000/docs`.
5. Проверь endpoint вручную.
6. Запусти тесты:

```bash
uv run pytest
```

7. Если что-то сломалось, прочитай ошибку и найди место проблемы.

## Уровень 1. Первый FastAPI-код

Цель: понять `FastAPI()`, декораторы и обычные `GET` endpoints.

### Задание 1. Root endpoint

Проверь текущий endpoint:

```text
GET /
```

Ожидаемый ответ:

```json
{
  "message": "Hello from FastAPI Cloud"
}
```

Самопроверка:

- endpoint виден в `/docs`;
- тег называется `root`;
- тест `test_home` проходит.

### Задание 2. Health check

Проверь endpoint:

```text
GET /health
```

Ожидаемый ответ:

```json
{
  "status": "ok"
}
```

Вопросы:

- зачем backend-приложению healthcheck?
- почему этот endpoint должен быть простым?
- какой status code должен быть при успехе?

## Уровень 2. Path и Query

Цель: понять разницу между path-параметром и query-параметром.

### Задание 3. Item by ID

Проверь endpoint:

```text
GET /items/5
```

Ожидаемый ответ:

```json
{
  "item_id": 5,
  "q": null
}
```

Теперь проверь:

```text
GET /items/5?q=somequery
```

Ожидаемый ответ:

```json
{
  "item_id": 5,
  "q": "somequery"
}
```

Вопросы:

- откуда FastAPI берет `item_id`?
- откуда FastAPI берет `q`?
- почему `q` может быть `null`?

### Задание 4. Ошибка 422

Открой:

```text
GET /items/not-an-int
```

Ожидаемый status code:

```text
422
```

Найди в ответе:

- `detail`;
- `loc`;
- `msg`;
- `input`.

Объясни своими словами, почему FastAPI вернул `422`.

## Уровень 3. Новые endpoints

Цель: научиться добавлять простые маршруты самостоятельно.

### Задание 5. Version endpoint

Добавь endpoint:

```text
GET /version
```

Ожидаемый ответ:

```json
{
  "version": "0.1.0"
}
```

Требования:

- добавь `tags=["meta"]`;
- добавь `summary`;
- добавь тест.

### Задание 6. Hello endpoint

Добавь endpoint:

```text
GET /hello/{name}
```

Пример:

```text
GET /hello/Anna
```

Ожидаемый ответ:

```json
{
  "message": "Hello, Anna"
}
```

Дополнительно:

- добавь query-параметр `uppercase: bool = False`;
- если `uppercase=true`, возвращай сообщение большими буквами.

## Уровень 4. Pydantic

Цель: научиться принимать JSON body.

### Задание 7. Book model

Создай Pydantic-модели:

```python
from pydantic import BaseModel, Field

class BookCreate(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    author: str = Field(min_length=1, max_length=80)

class BookRead(BookCreate):
    id: int
```

Добавь:

```text
POST /books
GET /books
GET /books/{book_id}
```

Требования:

- `POST /books` возвращает `201`;
- `GET /books/{book_id}` возвращает `404`, если книги нет;
- данные можно хранить в словаре в памяти;
- все endpoints имеют `tags=["books"]`.

## Уровень 5. Обновление и удаление

Цель: понять `PATCH`, `DELETE`, `exclude_unset=True`.

### Задание 8. Book update

Добавь модель:

```python
class BookUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=120)
    author: str | None = Field(default=None, min_length=1, max_length=80)
```

Добавь:

```text
PATCH /books/{book_id}
DELETE /books/{book_id}
```

Требования:

- `PATCH` обновляет только переданные поля;
- `DELETE` возвращает `204`;
- если книги нет, вернуть `404`;
- добавь тесты.

## Уровень 6. APIRouter

Цель: подготовиться к структуре большого приложения.

### Задание 9. Вынести books в router

Создай структуру:

```text
app/
├── __init__.py
├── main.py
└── routers/
    ├── __init__.py
    └── books.py
```

Перенеси books endpoints в `app/routers/books.py`.

Требования:

- используй `APIRouter`;
- подключи router через `include_router`;
- обнови `entrypoint` в `pyproject.toml`, если переносишь приложение из `main.py` в `app/main.py`;
- тесты должны проходить.

## Контрольный чеклист

После выполнения заданий ты должен уметь:

- объяснить `app = FastAPI(...)`;
- объяснить `@app.get`;
- отличать path от query;
- читать ошибку `422`;
- создавать Pydantic-модели;
- использовать `response_model`;
- возвращать `404` через `HTTPException`;
- писать простые тесты;
- понимать, зачем нужен `APIRouter`.
