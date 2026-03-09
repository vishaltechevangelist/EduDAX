class IngestionService:

    def __init__(self, pdf_loader, chunker, embedding_engine, vector_store):
        self.pdf_loader = pdf_loader
        self.chunker = chunker
        self.embedding_engine = embedding_engine
        self.vector_store = vector_store
        
    def ingest(self, pdf_path:str):
        pages = self.pdf_loader.load(pdf_path=pdf_path)

        chunks = self.chunker.chunk(pages)

        texts = [chunk["text"] for chunk in chunks]
        
        return self.embedding_engine.embed(texts)