import { useState, useEffect } from 'react'
import { getNotes, deleteNote, synthesizeNote } from '../api'

function NoteList() {
  const [notes, setNotes] = useState([])

  useEffect(() => {
    loadNotes()
  }, [])

  async function loadNotes() {
    const data = await getNotes()
    setNotes(data)
  }

  async function handleDelete(id) {
    await deleteNote(id)
    loadNotes()
  }

  async function handleSynthesize(id) {
    await synthesizeNote(id)
    loadNotes()
  }

  return (
    <ul>
      {notes.map(note => (
        <li key={note.id}>
          <strong>{note.title}</strong>
          <p>{note.text}</p>
          <button onClick={() => handleSynthesize(note.id)}>Sintetizar</button>
          {note.audio_path && (
            <audio controls src={`/api/notes/${note.id}/audio`} />
          )}
          <button onClick={() => handleDelete(note.id)}>Eliminar</button>
        </li>
      ))}
    </ul>
  )
}

export default NoteList
