from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from pathlib import Path

DB_DIR = "rag/db"

def ingest(pdf_path):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    db = Chroma.from_documents(
        docs,
        embeddings,
        persist_directory=DB_DIR
    )
    db.persist()