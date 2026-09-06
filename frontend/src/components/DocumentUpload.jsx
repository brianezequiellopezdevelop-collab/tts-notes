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
    <form onSubmit={handleSubmit}>
      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setFile(e.target.files[0])}
      />
      <button type="submit">Subir PDF</button>
    </form>
  )
}

export default DocumentUpload
