from pathlib import Path

from tinydb import TinyDB


DB_PATH = Path(__file__).resolve().parent.parent / "books_db.json"
TABLE_NAME = "books"


def get_db() -> TinyDB:
    return TinyDB(DB_PATH)
