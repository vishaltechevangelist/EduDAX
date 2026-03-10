import sys
from src.adapters.vectors.base_store import BaseVectorStore

class ChromaStore(BaseVectorStore):
    def __init__(self, client, collection):
        self.client = client
        self.collection = collection

    def add_documents(self, ids, texts, embeddings, metadata):
        self.collection.upsert(ids=ids, documents=texts, embeddings=embeddings, metadatas=metadata)
        return self.collection.count()

    def similarity_search(self):
        pass