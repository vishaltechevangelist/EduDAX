from src.services.ingestion_service import IngestionService
from src.ingestion.pdf_loader import PDFLoader
from src.ingestion.chunker import Chunker
from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.engines.embedding_engine import EmbeddingEngine
from sentence_transformers import SentenceTransformer
from src.adapters.vectors.chroma_store import ChromaStore
from src.repositories.vector_repositories import VectorRepository
import chromadb

from src.pipeline.question_generation_pipeline import QuestionGenerationPipeline
from src.services.query_service import QueryService
from src.retrievers.retriever import Retriever
from src.engines.embedding_engine import EmbeddingEngine
from src.adapters.llm.ollama_client import OllamaClient
from src.adapters.llm.prompt_builder import PromptBuilder


class EduFactory:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

            cls._instance._pdf_loader = None
            cls._instance._chunker = None
            cls._instance._text_splitter = None
            cls._instance._embedding_engine = None
            cls._instance._vector_store = None
            cls._instance._ingestion_service = None
            cls._instance._sentence_transformer = None
            cls._instance._vector_repository = None
            cls._instance._vector_store = None
            cls._instance._query_service = None
            cls._instance._question_generation_pipeline = None
            cls._instance._retriever = None
            cls._instance._llm_client = None
            cls._instance._prompt_builder = None

        return cls._instance
    
    def get_pdf_loader(self):
        if self._pdf_loader is None:
            self._pdf_loader = PDFLoader()
        return self._pdf_loader
        
    def get_text_splitter(self):
        if self._text_splitter is None:
            self._text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        return self._text_splitter

    def get_chunker(self):
        if self._chunker is None:
            self._chunker = Chunker(self.get_text_splitter())
        return self._chunker

    def get_sentence_transformer(self):
        if self._sentence_transformer is None:
            self._sentence_transformer = SentenceTransformer("BAAI/bge-small-en")
        return self._sentence_transformer

    def get_embedding_engine(self):
        if self._embedding_engine is None:
            self._embedding_engine = EmbeddingEngine(self.get_sentence_transformer())
        return self._embedding_engine

    def get_vector_store(self):
        if self._vector_store is None:
            client = chromadb.PersistentClient(path="data/chroma_db")
            collection = client.get_or_create_collection(name='ncert_kb')
            self._vector_store = ChromaStore(client, collection)
        return self._vector_store
    
    def get_vector_repository(self):
        if self._vector_repository is None:
            self._vector_repository = VectorRepository(self.get_vector_store())
        return self._vector_repository

    def get_ingestion_service(self):
        pdf_loader = self.get_pdf_loader()
        chunker = self.get_chunker()
        embedding_engine = self.get_embedding_engine()
        vector_repository = self.get_vector_repository()
        return IngestionService(pdf_loader, chunker, embedding_engine, vector_repository)

    def get_retriever(self):
        if self._retriever is None:
            self._retriever = Retriever(self.get_embedding_engine(), self.get_vector_repository())
        return self._retriever
    
    def get_llm_client(self):
        if self._llm_client is None:
            self._llm_client = OllamaClient()
        return self._llm_client

    def get_prompt_builder(self):
        if self._prompt_builder is None:
            self._prompt_builder = PromptBuilder()
        return self._prompt_builder

    def get_question_generation_pipeline(self):
        if self._question_generation_pipeline is None:
            self._question_generation_pipeline = QuestionGenerationPipeline(self.get_retriever(), self.get_prompt_builder(), self.get_llm_client())
        return self._question_generation_pipeline

    def get_query_service(self):
        if self._query_service is None:
            self._query_service = QueryService(self.get_question_generation_pipeline())
        return self._query_service
        
factory = EduFactory()