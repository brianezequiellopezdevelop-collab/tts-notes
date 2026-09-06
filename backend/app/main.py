# backend/app/main.py
import os
from app.heartbeat import start_watchdog
from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.routes import router
from app.db import init_db, init_documents_table

app = FastAPI(title="TTS Notes API")

init_db()
init_documents_table()
if os.environ.get("TTS_NOTES_STANDALONE") == "1":
    start_watchdog()

app.include_router(router, prefix="/api")

FRONTEND_DIST = Path(__file__).parent.parent.parent / "frontend" / "dist"
app.mount("/", StaticFiles(directory=FRONTEND_DIST, html=True), name="static")
