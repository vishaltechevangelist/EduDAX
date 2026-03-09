from src.services.ingestion_service import IngestionService
from src.adapters.vectors.chroma_store import ChromaStore
from src.engines.embedding_engine import EmbeddingEngine
from src.ingestion.pdf_loader import PDFLoader
from src.ingestion.chunker import Chunker

class EduFactory:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            cls._instance._pdf_loader = None
            cls._instance._chunker = None
            cls._instance._embedding_engine = None
            cls._instance._vector_store = None
            cls._instance._ingestion_service = None

        return cls._instance

    def get_chunker(self):
        if self._chunker is None:
            self._chunker = Chunker()
        return self._chunker
    
    def get_embedding_engine(self):
        if self._embedding_engine is None:
            self._embedding_engine = EmbeddingEngine()
        return self._embedding_engine

    def get_vector_store(self):
        if self._vector_store is None:
            self._vector_store = ChromaStore()
        return self._vector_store
    
    def get_pdf_loader(self):
        if self._pdf_loader is None:
            self._pdf_loader = PDFLoader()
        return self._pdf_loader
    
    def get_chunker(self):
        if self._chunker is None:
            self._chunker = Chunker()
        return self._chunker

    def get_ingestion_service(self):
        pdf_loader = self.get_pdf_loader()
        chunker = self.get_chunker()
        embedding_engine = self.get_embedding_engine()
        vector_store = self.get_vector_store()
        return IngestionService(pdf_loader, chunker, embedding_engine, vector_store)
        
factory = EduFactory()