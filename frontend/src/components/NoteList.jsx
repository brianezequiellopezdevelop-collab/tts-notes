import { useState, useEffect } from 'react'
import { Trash2 } from 'lucide-react'
import { getNotes, deleteNote, synthesizeNote } from '../api'
import AppAudioPlayer from './AudioPlayer'

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
    <ul className="space-y-3">
      {notes.map(note => (
        <li key={note.id} className="bg-[var(--surface)] p-4 rounded-lg shadow-sm border border-[var(--border)]">
          <div className="flex items-start justify-between gap-2">
            <div>
              <h3 className="font-semibold">{note.title}</h3>
              <p className="text-[var(--text-muted)] text-sm mt-1">{note.text}</p>
            </div>
            <button
              onClick={() => handleDelete(note.id)}
              aria-label="Eliminar nota"
              className="shrink-0 p-2 rounded-md text-[var(--danger)] hover:bg-[var(--danger-soft)] transition-colors"
            >
              <Trash2 size={18} />
            </button>
          </div>
          <button
            onClick={() => handleSynthesize(note.id)}
            className="mt-3 bg-[var(--primary-soft)] text-[var(--primary-soft-text)] px-3 py-1.5 rounded-md text-sm font-medium hover:opacity-80 transition-opacity"
          >
            Sintetizar
          </button>
         {note.audio_path && (
  <div className="mt-3">
    <AppAudioPlayer src={`/api/notes/${note.id}/audio`} />
  </div>
)}
        </li>
      ))}
    </ul>
  )
}

export default NoteList
