# backend/app/api/routes.py

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from app.db import get_connection
from app.schemas import NoteCreate, NoteResponse, NoteUpdate
from app.core.piper_engine import PiperEngine

router = APIRouter()
engine = PiperEngine("voices/es_ES-davefx-medium.onnx")


@router.post("/notes", response_model=NoteResponse)
def create_note(note: NoteCreate):
    conn = get_connection()
    cursor = conn.execute(
        "INSERT INTO notes (title, text) VALUES (?, ?)",
        (note.title, note.text)
    )
    conn.commit()
    new_id = cursor.lastrowid
    row = conn.execute("SELECT * FROM notes WHERE id = ?", (new_id,)).fetchone()
    conn.close()
    return dict(row)


@router.get("/notes", response_model=list[NoteResponse])
def list_notes():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM notes").fetchall()
    conn.close()
    return [dict(row) for row in rows]


@router.get("/notes/{note_id}", response_model=NoteResponse)
def get_note(note_id: int):
    conn = get_connection()
    row = conn.execute("SELECT * FROM notes WHERE id = ?", (note_id,)).fetchone()
    conn.close()
    if row is None:
        raise HTTPException(status_code=404, detail="Nota no encontrada")
    return dict(row)


@router.post("/notes/{note_id}/synthesize", response_model=NoteResponse)
def synthesize_note(note_id: int):
    conn = get_connection()
    row = conn.execute("SELECT * FROM notes WHERE id = ?", (note_id,)).fetchone()
    if row is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Nota no encontrada")

    audio_path = f"data/audio_{note_id}.wav"
    engine.synthesize(row["text"], audio_path)

    conn.execute(
        "UPDATE notes SET audio_path = ?, voice = ? WHERE id = ?",
        (audio_path, "es_ES-davefx-medium", note_id)
    )
    conn.commit()
    updated_row = conn.execute("SELECT * FROM notes WHERE id = ?", (note_id,)).fetchone()
    conn.close()
    return dict(updated_row)


@router.get("/notes/{note_id}/audio")
def get_audio(note_id: int):
    conn = get_connection()
    row = conn.execute("SELECT * FROM notes WHERE id = ?", (note_id,)).fetchone()
    conn.close()
    if row is None or row["audio_path"] is None:
        raise HTTPException(status_code=404, detail="Audio no generado todavía")
    return FileResponse(row["audio_path"], media_type="audio/wav")
@router.patch("/notes/{note_id}", response_model=NoteResponse)
def update_note(note_id: int, note: NoteUpdate):
    conn = get_connection()
    existing = conn.execute("SELECT * FROM notes WHERE id = ?", (note_id,)).fetchone()
    if existing is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Nota no encontrada")

    new_title = note.title if note.title is not None else existing["title"]
    new_text = note.text if note.text is not None else existing["text"]

    conn.execute(
        "UPDATE notes SET title = ?, text = ? WHERE id = ?",
        (new_title, new_text, note_id)
    )
    conn.commit()
    updated_row = conn.execute("SELECT * FROM notes WHERE id = ?", (note_id,)).fetchone()
    conn.close()
    return dict(updated_row)


@router.delete("/notes/{note_id}")
def delete_note(note_id: int):
    conn = get_connection()
    existing = conn.execute("SELECT * FROM notes WHERE id = ?", (note_id,)).fetchone()
    if existing is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Nota no encontrada")

    conn.execute("DELETE FROM notes WHERE id = ?", (note_id,))
    conn.commit()
    conn.close()
    return {"detail": "Nota eliminada"}
