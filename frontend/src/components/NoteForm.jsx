import { useState } from 'react'
import { createNote } from '../api'


function NoteForm({ onNoteCreated }) {
  const [title, setTitle] = useState('')
  const [text, setText] = useState('')

  async function handleSubmit(e) {
    e.preventDefault()
    await createNote(title, text)
    setTitle('')
    setText('')
    onNoteCreated()
  }

  return (
    <form onSubmit={handleSubmit} className="bg-[var(--surface)] p-6 rounded-lg shadow-sm border border-[var(--border)] space-y-3">
      <input
        type="text"
        placeholder="Título"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        className="w-full px-3 py-2 bg-[var(--bg)] text-[var(--text)] border border-[var(--border)] rounded-md focus:outline-none focus:ring-2 focus:ring-[var(--primary)]"
      />
      <textarea
        placeholder="Texto de la nota"
        value={text}
        onChange={(e) => setText(e.target.value)}
        rows={3}
        className="w-full px-3 py-2 bg-[var(--bg)] text-[var(--text)] border border-[var(--border)] rounded-md focus:outline-none focus:ring-2 focus:ring-[var(--primary)]"
      />
      <button
        type="submit"
        className="bg-[var(--primary)] text-white px-4 py-2 rounded-md font-medium hover:bg-[var(--primary-hover)] transition-colors"
      >
        Crear nota
      </button>
    </form>
  )
}

export default NoteForm
