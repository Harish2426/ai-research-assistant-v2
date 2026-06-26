from sentence_transformers import SentenceTransformer


class EmbeddingModel:

    def __init__(self):
        print("Loading embedding model...")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        print("Embedding model loaded!")

    def encode(self, text):
        return self.model.encode(text)

    def encode_many(self, texts):
        return self.model.encode(texts)


embedding_model = EmbeddingModel()