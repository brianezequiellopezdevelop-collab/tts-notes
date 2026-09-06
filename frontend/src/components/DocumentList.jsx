import { useState, useEffect } from 'react'
import { getDocuments, synthesizeDocument } from '../api'

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

  return (
    <ul>
      {documents.map(doc => (
        <li key={doc.id}>
          <strong>{doc.filename}</strong>
          <button onClick={() => handleSynthesize(doc.id)}>Sintetizar</button>
          {doc.audio_path && (
            <audio controls src={`/api/documents/${doc.id}/audio`} />
          )}
        </li>
      ))}
    </ul>
  )
}

export default DocumentList
