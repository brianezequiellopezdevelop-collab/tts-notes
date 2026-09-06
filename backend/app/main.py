# backend/app/main.py

from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="TTS Notes API")

app.include_router(router)


@app.get("/")
def health():
    return {"status": "ok"}
