// frontend/src/components/DocumentUpload.jsx
import { useState } from 'react'
import { uploadDocument } from '../api'

function DocumentUpload({ onDocumentUploaded }) {
  const [file, setFile] = useState(null)

  async function handleSubmit(e) {
    e.preventDefault()
    if (!file) return
    await uploadDocument(file)
    setFile(null)
    onDocumentUploaded()
  }

  return (
    <form onSubmit={handleSubmit} className="bg-[var(--surface)] p-6 rounded-lg shadow-sm border border-[var(--border)] flex items-center gap-3">
      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setFile(e.target.files[0])}
        className="flex-1 text-sm text-[var(--text-muted)] file:mr-3 file:py-2 file:px-4 file:rounded-md file:border-0 file:bg-[var(--primary-soft)] file:text-[var(--primary-soft-text)] file:font-medium hover:file:opacity-80"
      />
      <button
        type="submit"
        className="bg-[var(--primary)] text-white px-4 py-2 rounded-md font-medium hover:bg-[var(--primary-hover)] transition-colors whitespace-nowrap"
      >
        Subir PDF
      </button>
    </form>
  )
}

export default DocumentUpload
