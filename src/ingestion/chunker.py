import re

class Chunker:
    def __init__(self, splitter):
        self.splitter = splitter

    def chunk(self, text):
        text = self.clean_text(text)
        sections = self.split_by_headings(text)

        chunks = []

        for section in sections:
            content = section["content"]

            # fallback splitter if section too large
            if len(content) > 800:
                split_chunks = self.splitter.split_text(content)

                for chunk in split_chunks:
                    chunks.append({
                        "topic": section["topic"],
                        "subtopic": section["subtopic"],
                        "text": chunk
                    })
            else:
                chunks.append({
                    "topic": section["topic"],
                    "subtopic": section["subtopic"],
                    "text": content
                })

        return chunks

    def split_by_headings(self, text):

        # NCERT friendly heading patterns
        pattern = r'(\n\d+\.\d+.*|\n[A-Z][A-Z\s]{5,}\n)'

        parts = re.split(pattern, text)

        sections = []
        current_topic = None

        for part in parts:
            if not part.strip():
                continue

            if re.match(pattern, part):
                current_topic = part.strip()
            else:
                sections.append({
                    "topic": current_topic,
                    "subtopic": None,
                    "content": part.strip()
                })

        return sections
    
    def clean_text(self, text):
        text = re.sub(r'Activity\s+\d+(\.\d+)?', '', text)
        text = re.sub(r'Figure\s+\d+(\.\d+)?', '', text)
        text = re.sub(r'Table\s+\d+(\.\d+)?', '', text)
        return text