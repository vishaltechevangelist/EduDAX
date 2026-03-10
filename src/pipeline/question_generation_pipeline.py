class QuestionGenerationPipeline:
    def __init__(self, retriever, prompt_builder, llm):
        self.retriever = retriever
        self.prompt_builder = prompt_builder
        self.llm = llm
        
    def generate(self, request):
        filters = {
            "class_name": request.class_name,
            "subject": request.subject,
            "chapter": request.chapter
        }
        results = self.retriever.retrieve(filters)
        # print(chunks)
        prompt = self.prompt_builder.build(results['documents'], request)
        response = self.llm.generate(prompt)
        return response