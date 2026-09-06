# backend/app/main.py

from fastapi import FastAPI
from app.api.routes import router
from app.db import init_db, init_documents_table

app = FastAPI(title="TTS Notes API")

init_db()
init_documents_table()

@app.get("/")
def health():
    return {"status": "ok"}
    

app.include_router(router, prefix="/api")
