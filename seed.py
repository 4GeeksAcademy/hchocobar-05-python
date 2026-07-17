from tinydb import Query

from app.db import TABLE_NAME, get_db


SEED_BOOKS = [
    {
        "title": "The Pragmatic Programmer",
        "author": "Hunt & Thomas",
        "genre": "non-fiction",
        "pages": 352,
        "status": "available",
    },
    {
        "title": "Dune",
        "author": "Frank Herbert",
        "genre": "sci-fi",
        "pages": 412,
        "status": "available",
    },
    {
        "title": "The Big Sleep",
        "author": "Raymond Chandler",
        "genre": "mystery",
        "pages": 231,
        "status": "checked_out",
    },
    {
        "title": "Nineteen Eighty-Four",
        "author": "George Orwell",
        "genre": "fiction",
        "pages": 328,
        "status": "available",
    },
]


def seed_books() -> int:
    db = get_db()
    books = db.table(TABLE_NAME)
    book_query = Query()
    inserted = 0

    try:
        for book in SEED_BOOKS:
            exists = books.contains(
                (book_query.title == book["title"]) & (book_query.author == book["author"])
            )
            if not exists:
                books.insert(book)
                inserted += 1
    finally:
        db.close()

    return inserted


if __name__ == "__main__":
    inserted_count = seed_books()
    print(f"Inserted {inserted_count} records.")
