from sentence_transformers import SentenceTransformer
import torch

MODEL_NAME = "all-MiniLM-L6-v2"

class EmbeddingService:
    def __init__(self):
        self.device = "cpu"
        self.model = SentenceTransformer(MODEL_NAME, device=self.device)

    def embed(self, texts: list[str]):
        with torch.no_grad():
            return self.model.encode(
                texts,
                normalize_embeddings=True,
                device=self.device
            )
