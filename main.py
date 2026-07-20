from fastapi import FastAPI

from app.routers import auth, profiles, users


app = FastAPI(title="API de Intercambio de Plantas")

app.include_router(users.router)
app.include_router(profiles.router)
app.include_router(auth.router)


@app.get("/")
def health() -> dict[str, str]:
    return {"status": "ok"}
