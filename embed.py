import os
import chromadb
from sentence_transformers import SentenceTransformer
from utils import load_and_split_documents

persist_directory = "chroma_storage"
pdf_folder = "data/acts"

def embed_documents():
    print("Loading embedding model...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    print("Loading and splitting documents...")
    documents, metadatas = load_and_split_documents(pdf_folder)

    print("Embedding documents...")
    embeddings = model.encode(documents).tolist()

    client = chromadb.PersistentClient(path=persist_directory)
    collection = client.get_or_create_collection(name="indian_laws")
    ids = [str(i) for i in range(len(documents))]

    #collection.add(documents=documents, embeddings=embeddings, metadatas=metadatas, ids=ids)
    batch_size = 500
    for i in range(0, len(documents), batch_size):
        collection.add(
            documents=documents[i:i+batch_size],
            embeddings=embeddings[i:i+batch_size],
            metadatas=metadatas[i:i+batch_size],
            ids=ids[i:i+batch_size],
    )

    print(f"Embedded {len(documents)} chunks.")

if __name__ == "__main__":
    embed_documents()
