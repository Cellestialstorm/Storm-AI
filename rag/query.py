from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from llm.model import ask_llm

DB_DIR = "rag/db"

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory=DB_DIR,
    embedding_function=embeddings
)

def ask_rag(question: str) -> str:
    docs = db.similarity_search(question, k=3)
    context = "\n\n".join(d.page_content for d in docs)

    prompt = f"""
Answer ONLY using the context below.
If the answer is not in context, say you don't know.

Context:
{context}

Question:
{question}
"""

    return ask_llm(prompt)