class QueryService:
    def __init__(self, question_generation_pipeline):
        self.question_generation_pipeline = question_generation_pipeline
    
    def generate(self, request):
        return self.question_generation_pipeline.generate(request)