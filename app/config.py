from functools import lru_cache
import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    def __init__(self) -> None:
        self.secret_key = os.getenv("SECRET_KEY")
        self.algorithm = os.getenv("JWT_ALGORITHM", "HS256")
        expire_minutes = os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30")
        self.access_token_expire_minutes = int(expire_minutes)

        if not self.secret_key:
            raise RuntimeError("Falta SECRET_KEY en variables de entorno")


@lru_cache
def get_settings() -> Settings:
    return Settings()
