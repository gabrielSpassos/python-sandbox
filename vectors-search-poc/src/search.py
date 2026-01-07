import faiss
import json
from src.embeddings import EmbeddingService

class VectorSearch:
    def __init__(self):
        self.embedder = EmbeddingService()
        self.index = faiss.read_index("data/index.faiss")

        with open("data/documents.json") as f:
            self.documents = json.load(f)

    def search(self, query: str, k: int = 5):
        query_vector = self.embedder.embed([query])
        distances, indices = self.index.search(query_vector, k)

        results = []
        for idx, score in zip(indices[0], distances[0]):
            if idx == -1:
                continue
            results.append({
                "id": self.documents[idx]["id"],
                "text": self.documents[idx]["text"],
                "score": float(score)
            })

        return results
