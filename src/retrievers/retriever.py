class Retriever:
    def __init__(self, embedding_engine, vector_repository):
        self.embedding_engine = embedding_engine
        self.vector_repository = vector_repository

    def retrieve(self, filters):
        return self.vector_repository.filter_search(filters)