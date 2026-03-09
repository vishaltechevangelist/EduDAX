from src.factory import factory

ingestion_service = factory.get_ingestion_service()
result = ingestion_service.ingest("data/raw_pdfs/iesc101.pdf")
print(result)