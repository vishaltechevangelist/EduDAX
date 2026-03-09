import fitz
from tqdm import tqdm
from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
import chromadb

# -----------------------
# Configuration
# -----------------------

PDF_PATH = "data/raw_pdfs/iesc101.pdf"
CHROMA_PATH = "data/chroma_db"
COLLECTION_NAME = "ncert_kb"

# -----------------------
# Load PDF
# -----------------------

def load_pdf(path):
    doc = fitz.open(path)
    pages = []

    for page_num, page in enumerate(doc):
        text = page.get_text()
        pages.append((page_num + 1, text))

    return pages


# -----------------------
# Chunk Text
# -----------------------

def chunk_text(pages):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = []

    for page_num, text in pages:
        page_chunks = splitter.split_text(text)

        for chunk in page_chunks:
            chunks.append({
                "text": chunk,
                "page": page_num
            })

    return chunks


# -----------------------
# Embedding Model
# -----------------------

model = SentenceTransformer("BAAI/bge-small-en")


# -----------------------
# Chroma Setup
# -----------------------

client = chromadb.Client(
    chromadb.config.Settings(
        persist_directory=CHROMA_PATH
    )
) 

collection = client.get_or_create_collection(COLLECTION_NAME)


# -----------------------
# Ingestion
# -----------------------

def ingest():

    pages = load_pdf(PDF_PATH)

    chunks = chunk_text(pages)

    for i, chunk in enumerate(tqdm(chunks)):

        embedding = model.encode(chunk["text"]).tolist()

        collection.add(
            ids=[f"chunk_{i}"],
            documents=[chunk["text"]],
            embeddings=[embedding],
            metadatas=[{
                "page": chunk["page"],
                "source": "NCERT"
            }]
        )
    client.persist()
    print("Ingestion completed")


if __name__ == "__main__":
    ingest()