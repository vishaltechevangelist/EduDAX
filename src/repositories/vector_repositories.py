class VectorRepository:
    def __init__(self, vector_store):
        self.vector_store = vector_store

    def save_chunks(self, chunks, embeddings, metadata):
        ids = []
        texts = []
        metadata_list = []

        for i, chunk in enumerate(chunks):
            ids.append(f"{metadata['class_name']}_{metadata['subject']}_{metadata['chapter']}_chunk_{i}")
            texts.append(chunk["text"])
            metadata["topic"] = chunk["topic"]
            metadata["subtopic"] = chunk["subtopic"]
            metadata_list.append(metadata)

        return self.vector_store.add_documents(ids=ids, texts=texts, embeddings=embeddings, metadata=metadata_list)
    
    def search(self, filters, top_k=5):
        return self.vector_store.similarity_search(filters)
    
    def filter_search(self, filters, limit=20):
        return self.vector_store.filter_search(filters, limit)

        