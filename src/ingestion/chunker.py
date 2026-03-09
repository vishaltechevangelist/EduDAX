class Chunker:
    def __init__(self, splitter):
        self.splitter = splitter
    
    def chunk(self, pages):
        chunks = []

        for page in pages:
            page_number = page["page"]
            text = page["text"]

            split_chunks = self.splitter.split_text(text=text)

            for chunk in split_chunks:
                chunks.append({"text":chunk, "page":page_number})

        return chunks