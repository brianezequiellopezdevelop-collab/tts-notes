# backend/app/schemas.py

from pydantic import BaseModel
from typing import Optional


class NoteCreate(BaseModel):
    title: str
    text: str


class NoteResponse(BaseModel):
    id: int
    title: str
    text: str
    voice: Optional[str] = None
    audio_path: Optional[str] = None
    created_at: str


class NoteUpdate(BaseModel):
    title: Optional[str] = None
    text: Optional[str] = None
