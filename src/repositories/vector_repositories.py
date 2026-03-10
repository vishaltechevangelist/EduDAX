class VectorRepository:
    def __init__(self, vector_store):
        self.vector_store = vector_store

    def save_chunks(self, chunks, embeddings):
        ids = []
        texts = []
        metadata = []

        for i, chunk in enumerate(chunks):
            ids.append(f"chunk_{i}")
            texts.append(chunk["text"])
            metadata.append({"page": chunk["page"], "source":"NCERT"})

        return self.vector_store.add_documents(ids=ids, texts=texts, embeddings=embeddings, metadata=metadata)