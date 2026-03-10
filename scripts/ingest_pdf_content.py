from src.factory import factory

ingestion_service = factory.get_ingestion_service()
class_name = 'class9'
subject = 'science'
chapter = 'chapter1'
result = ingestion_service.ingest(f"data/raw_pdfs/{class_name}/{subject}/{chapter}.pdf", 
                                  metadata={"class_name":class_name, "subject":subject, "chapter":chapter})
print(result)