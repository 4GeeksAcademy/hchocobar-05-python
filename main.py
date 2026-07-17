from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Query
from tinydb import Query as TinyQuery

from app.db import TABLE_NAME, get_db
from app.models import Book, BookGenre, BookResponse, BookStatus, BookStatusUpdate
from seed import seed_books


@asynccontextmanager
async def lifespan(app: FastAPI):
    seed_books()
    yield


app = FastAPI(title="Books Catalog API", lifespan=lifespan)


def to_book_response(document: dict, doc_id: int) -> BookResponse:
    return BookResponse(id=doc_id, **document)


@app.post("/books", response_model=BookResponse, status_code=201)
def create_book(book: Book):
    db = get_db()
    books = db.table(TABLE_NAME)

    try:
        payload = book.model_dump(mode="json")
        doc_id = books.insert(payload)
        created = books.get(doc_id=doc_id)
    finally:
        db.close()

    return to_book_response(created, doc_id)


@app.get("/books", response_model=list[BookResponse])
def list_books(
    genre: BookGenre | None = Query(default=None),
    status: BookStatus | None = Query(default=None),
):
    db = get_db()
    books = db.table(TABLE_NAME)
    book_query = TinyQuery()

    try:
        if genre is None and status is None:
            documents = books.all()
        else:
            condition = None
            if genre is not None:
                condition = book_query.genre == genre.value
            if status is not None:
                status_condition = book_query.status == status.value
                condition = status_condition if condition is None else (condition & status_condition)
            documents = books.search(condition)
    finally:
        db.close()

    return [to_book_response(doc, doc.doc_id) for doc in documents]


@app.get("/books/{book_id}", response_model=BookResponse)
def get_book(book_id: int):
    db = get_db()
    books = db.table(TABLE_NAME)

    try:
        document = books.get(doc_id=book_id)
    finally:
        db.close()

    if document is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return to_book_response(document, book_id)


@app.patch("/books/{book_id}/status", response_model=BookResponse)
def update_book_status(book_id: int, payload: BookStatusUpdate):
    db = get_db()
    books = db.table(TABLE_NAME)

    try:
        existing = books.get(doc_id=book_id)
        if existing is None:
            raise HTTPException(status_code=404, detail="Book not found")

        books.update({"status": payload.status.value}, doc_ids=[book_id])
        updated = books.get(doc_id=book_id)
    finally:
        db.close()

    return to_book_response(updated, book_id)


@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    db = get_db()
    books = db.table(TABLE_NAME)

    try:
        existing = books.get(doc_id=book_id)
        if existing is None:
            raise HTTPException(status_code=404, detail="Book not found")

        books.remove(doc_ids=[book_id])
    finally:
        db.close()

    return {"detail": "Book deleted"}
