# rag_setup.py

from sentence_transformers import SentenceTransformer
import faiss
import os
from pathlib import Path
import pickle
import fitz  # PyMuPDF

# Load PDF and extract text using PyMuPDF
pdf_path = r"C:\Users\IT SHOP\Downloads\Documents\Hands-On Large Language Models Language Understanding and Generation (Jay Alammar, Maarten Grootendorst) .pdf"
text = ""

with fitz.open(pdf_path) as doc:
    for page in doc:
        text += page.get_text()

# Split text into chunks
def split_text(text, max_length=500):
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]

chunks = split_text(text)

# Load embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Create embeddings
embeddings = model.encode(chunks)

# Build FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save index and chunks
faiss.write_index(index, "vector.index")
with open("chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)


def retrieve_answer(query):
    # your RAG logic here
    return "Your generated answer"


print("✅ RAG setup completed: vector.index and chunks.pkl saved.")