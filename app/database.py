from pathlib import Path

from tinydb import Query, TinyDB


DB_PATH = Path(__file__).resolve().parent.parent / "db.json"

db = TinyDB(DB_PATH)
users_table = db.table("users")
profiles_table = db.table("profiles")

UserQuery = Query()
ProfileQuery = Query()


def get_user_by_email(email: str) -> dict | None:
    return users_table.get(UserQuery.email == email)


def get_user_by_id(user_id: str) -> dict | None:
    return users_table.get(UserQuery.id == user_id)


def get_profile_by_user_id(user_id: str) -> dict | None:
    return profiles_table.get(ProfileQuery.user_id == user_id)
