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
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Título"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />
      <textarea
        placeholder="Texto de la nota"
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button type="submit">Crear nota</button>
    </form>
  )
}

export default NoteForm
