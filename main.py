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
