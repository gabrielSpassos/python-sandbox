from fastapi import FastAPI
from src.search import VectorSearch

app = FastAPI(title="Vector Search PoC")
search_engine = VectorSearch()

@app.get("/search")
def search(q: str, k: int = 5):
    return {
        "query": q,
        "results": search_engine.search(q, k)
    }
