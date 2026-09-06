# backend/test_db.py

from app.db import get_connection, init_db

init_db()

conn = get_connection()

# Crear una nota
conn.execute(
    "INSERT INTO notes (title, text) VALUES (?, ?)",
    ("Mi primera nota", "Este es un texto de prueba para convertir a audio.")
)
conn.commit()

# Leer todas las notas
rows = conn.execute("SELECT * FROM notes").fetchall()
for row in rows:
    print(dict(row))

conn.close()
