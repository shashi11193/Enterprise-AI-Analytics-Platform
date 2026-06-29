import os
import fitz  # PyMuPDF
from ingestion.config import PDF_DIR


def load_pdf(file_name: str):
    path = os.path.join(PDF_DIR, file_name)

    doc = fitz.open(path)

    text = ""

    for page in doc:
        text += page.get_text()

    return text


def load_all_pdfs():
    docs = {}

    for file in os.listdir(PDF_DIR):
        if file.endswith(".pdf"):
            docs[file] = load_pdf(file)

    return docs