class EmbeddingEngine:
    def __init__(self, sentence_transformer):
        self.sentence_transformer = sentence_transformer

    def embed(self, texts):
        embeddings = self.sentence_transformer.encode(texts, batch_size=32)
        return embeddings.tolist()
