class IngestionService:

    def __init__(self, pdf_loader, chunker, embedding_engine, vector_repositories):
        self.pdf_loader = pdf_loader
        self.chunker = chunker
        self.embedding_engine = embedding_engine
        self.vector_repositories = vector_repositories
        
    def ingest(self, pdf_path:str):
        pages = self.pdf_loader.load(pdf_path=pdf_path)

        chunks = self.chunker.chunk(pages)

        texts = [chunk["text"] for chunk in chunks]
        
        embeddings = self.embedding_engine.embed(texts)

        return self.vector_repositories.save_chunks(chunks, embeddings)
