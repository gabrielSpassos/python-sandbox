import faiss
import json
from src.embeddings import EmbeddingService

DIMENSION = 384

def build_index(documents):
    embedder = EmbeddingService()
    vectors = embedder.embed([doc["text"] for doc in documents])

    index = faiss.IndexHNSWFlat(DIMENSION, 32)
    index.hnsw.efConstruction = 200
    index.add(vectors)

    return index, vectors

if __name__ == "__main__":
    with open("data/documents.json") as f:
        docs = json.load(f)

    index, _ = build_index(docs)
    faiss.write_index(index, "data/index.faiss")
