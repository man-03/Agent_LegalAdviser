import os
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def split_text(text, chunk_size=1000, overlap=200):
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def load_and_split_documents(pdf_folder):
    all_chunks = []
    metadatas = []
    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            path = os.path.join(pdf_folder, filename)
            print(f"Processing {filename}...")
            text = extract_text_from_pdf(path)
            chunks = split_text(text)
            all_chunks.extend(chunks)
            metadatas.extend([{"source": filename}] * len(chunks))
    return all_chunks, metadatas
