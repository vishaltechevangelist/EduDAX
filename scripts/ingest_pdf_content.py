from src.factory import factory

ingestion_service = factory.get_ingestion_service()
pages = ingestion_service.ingest("data/raw_pdfs/iesc101.pdf")
print(pages)