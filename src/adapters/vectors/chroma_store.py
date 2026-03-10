import sys
from src.adapters.vectors.base_store import BaseVectorStore

class ChromaStore(BaseVectorStore):
    def __init__(self, client, collection):
        self.client = client
        self.collection = collection

    def add_documents(self, ids, texts, embeddings, metadata):
        self.collection.upsert(ids=ids, documents=texts, embeddings=embeddings, metadatas=metadata)
        return self.collection.count()

    def similarity_search(self, filters):
        # print(filters)
        results = self.collection.get(where=filters)
        return results
    
    def filter_search(self, filters, limit=20):
        where_clause = {
                "$and": [
                    {key: value}
                    for key, value in filters.items()
                ]
            }
        results = self.collection.get(where=where_clause, limit=limit)
        # print(results)
        return results
    
    def debug_chroma(self):
        results = self.collection.get(where={
                            "$and": [
                                {"class_name": "class9"},
                                {"subject": "science"},
                                {"chapter": "chapter1"}
                            ]
                        }
                   )
        # results = self.collection.get(where=
        #                     #    {"chapter": "chapter1"}
        #                     )
        # return results.keys()
        return results