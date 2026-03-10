from abc import ABC, abstractmethod

class BaseVectorStore(ABC):
    @abstractmethod
    def add_documents(self, ids, texts, embeddings, metadata):
        pass

    @abstractmethod
    def similarity_search(self, query_embedding, k=5):
        pass