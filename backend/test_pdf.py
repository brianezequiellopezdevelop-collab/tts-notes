# backend/test_pdf.py

from pypdf import PdfReader

reader = PdfReader("test.pdf")

text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

print(text)
