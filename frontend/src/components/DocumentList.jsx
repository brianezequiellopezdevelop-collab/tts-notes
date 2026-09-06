import { useState, useEffect } from 'react'
import { Trash2 } from 'lucide-react'
import { getDocuments, synthesizeDocument, deleteDocument } from '../api'
import AppAudioPlayer from './AudioPlayer'

function DocumentList() {
  const [documents, setDocuments] = useState([])

  useEffect(() => {
    loadDocuments()
  }, [])

  async function loadDocuments() {
    const data = await getDocuments()
    setDocuments(data)
  }

  async function handleSynthesize(id) {
    await synthesizeDocument(id)
    loadDocuments()
  }

  async function handleDelete(id) {
    await deleteDocument(id)
    loadDocuments()
  }

  return (
    <ul className="space-y-3">
      {documents.map(doc => (
        <li key={doc.id} className="bg-[var(--surface)] p-4 rounded-lg shadow-sm border border-[var(--border)]">
          <div className="flex items-start justify-between gap-2">
            <h3 className="font-semibold">{doc.filename}</h3>
            <button
              onClick={() => handleDelete(doc.id)}
              aria-label="Eliminar documento"
              className="shrink-0 p-2 rounded-md text-[var(--danger)] hover:bg-[var(--danger-soft)] transition-colors"
            >
              <Trash2 size={18} />
            </button>
          </div>
          <button
            onClick={() => handleSynthesize(doc.id)}
            className="mt-3 bg-[var(--primary-soft)] text-[var(--primary-soft-text)] px-3 py-1.5 rounded-md text-sm font-medium hover:opacity-80 transition-opacity"
          >
            Sintetizar
          </button>
          {doc.audio_path && (
            <div className="mt-3">
              <AppAudioPlayer src={`/api/documents/${doc.id}/audio`} />
            </div>
          )}
        </li>
      ))}
    </ul>
  )
}

export default DocumentList
