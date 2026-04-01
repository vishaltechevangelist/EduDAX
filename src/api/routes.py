from fastapi import APIRouter
from src.api.schema import QueryRequest
from src.factory import factory
import json

router = APIRouter()

@router.post("/generate-questions")
def generate_questions(request: QueryRequest):
    query_service = factory.get_query_service()
    response = query_service.generate(request)
    return json.loads(response)

@router.get("/debug-chroma")
def inspect_chroma():
    store = factory.get_vector_store()
    results = store.debug_chroma()
    print(results["documents"][:3])
    print(results["metadatas"][:3])