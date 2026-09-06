const BASE_URL = '/api'

export async function getNotes() {
  const response = await fetch(`${BASE_URL}/notes`)
  return response.json()
}

export async function createNote(title, text) {
  const response = await fetch(`${BASE_URL}/notes`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ title, text })
  })
  return response.json()
}

export async function deleteNote(id) {
  await fetch(`${BASE_URL}/notes/${id}`, { method: 'DELETE' })
}

export async function synthesizeNote(id) {
  const response = await fetch(`${BASE_URL}/notes/${id}/synthesize`, {
    method: 'POST'
  })
  return response.json()
}

export async function getDocuments() {
  const response = await fetch(`${BASE_URL}/documents`)
  return response.json()
}

export async function uploadDocument(file) {
  const formData = new FormData()
  formData.append('file', file)
  const response = await fetch(`${BASE_URL}/documents`, {
    method: 'POST',
    body: formData
  })
  return response.json()
}

export async function synthesizeDocument(id) {
  const response = await fetch(`${BASE_URL}/documents/${id}/synthesize`, {
    method: 'POST'
  })
  return response.json()
}
