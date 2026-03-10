from pydantic import BaseModel

class QueryRequest(BaseModel):
    class_name: str
    subject: str
    chapter: str
    num_questions: int = 5
    question_type: str = "mcq"

    def to_filters(self):
        return {
            "class_name": self.class_name,
            "subject": self.subject,
            "chapter": self.chapter
        }
