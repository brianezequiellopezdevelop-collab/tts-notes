# backend/app/api/routes.py

import os

from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.responses import FileResponse
from pathlib import Path

from app.db import get_connection
from app.schemas import NoteCreate, NoteResponse, NoteUpdate, DocumentResponse
from app.core.piper_engine import PiperEngine
from pypdf import PdfReader

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

@router.post("/documents", response_model=DocumentResponse)
def upload_document(file: UploadFile = File(...)):
    file_path = f"data/pdfs/{file.filename}"
    Path("data/pdfs").mkdir(parents=True, exist_ok=True)

    with open(file_path, "wb") as f:
        f.write(file.file.read())

    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    conn = get_connection()
    cursor = conn.execute(
        "INSERT INTO documents (filename, file_path, extracted_text) VALUES (?, ?, ?)",
        (file.filename, file_path, text)
    )
    conn.commit()
    new_id = cursor.lastrowid
    row = conn.execute("SELECT * FROM documents WHERE id = ?", (new_id,)).fetchone()
    conn.close()
    return dict(row)


@router.get("/documents", response_model=list[DocumentResponse])
def list_documents():
    conn = get_connection()
    rows = conn.execute("SELECT * FROM documents").fetchall()
    conn.close()
    return [dict(row) for row in rows]


@router.post("/documents/{doc_id}/synthesize", response_model=DocumentResponse)
def synthesize_document(doc_id: int):
    conn = get_connection()
    row = conn.execute("SELECT * FROM documents WHERE id = ?", (doc_id,)).fetchone()
    if row is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Documento no encontrado")

    if not row["extracted_text"]:
        conn.close()
        raise HTTPException(status_code=400, detail="El documento no tiene texto extraible (podria ser un PDF escaneado)")

    audio_path = f"data/audio_doc_{doc_id}.wav"
    engine.synthesize(row["extracted_text"], audio_path)

    conn.execute(
        "UPDATE documents SET audio_path = ?, voice = ? WHERE id = ?",
        (audio_path, "es_ES-davefx-medium", doc_id)
    )
    conn.commit()
    updated_row = conn.execute("SELECT * FROM documents WHERE id = ?", (doc_id,)).fetchone()
    conn.close()
    return dict(updated_row)


@router.get("/documents/{doc_id}/audio")
def get_document_audio(doc_id: int):
    conn = get_connection()
    row = conn.execute("SELECT * FROM documents WHERE id = ?", (doc_id,)).fetchone()
    conn.close()
    if row is None or row["audio_path"] is None:
        raise HTTPException(status_code=404, detail="Audio no generado todavia")
    return FileResponse(row["audio_path"], media_type="audio/wav")
    
    
@router.delete("/documents/{doc_id}")
def delete_document(doc_id: int):
    conn = get_connection()
    row = conn.execute("SELECT * FROM documents WHERE id = ?", (doc_id,)).fetchone()
    if row is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Documento no encontrado")

    conn.execute("DELETE FROM documents WHERE id = ?", (doc_id,))
    conn.commit()
    conn.close()
    return {"detail": "Documento eliminado"}
