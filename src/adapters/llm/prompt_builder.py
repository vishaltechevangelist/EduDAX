class PromptBuilder:
    def build(self, chunks, request):
        context = "\n\n".join(chunks)

        instruction = f"Generate {request.num_questions} {request.question_type} questions for class {request.class_name} subject {request.subject} chapter {request.chapter}"

        prompt = f"""Role:  You are CBSE question generator
                     Context: {context}
                     Task: {instruction}

                     Requirements:
                        - Each question must have exactly 4 options
                        - Only one option should be correct
                        - Questions must be based only on the context
                        - Avoid repeating the same concept
                    
                     Return strictly valid JSON in the following format:
                            {{
                            "questions": [
                               {{
                                "id": 1,
                                "question": "Question text",
                                "level": easy | medium | hard  
                                "options": {{
                                    "A": "Option A",
                                    "B": "Option B",
                                    "C": "Option C",
                                    "D": "Option D"
                                }},
                                "correct_answer": "A"
                                }}
                            ]
                            }}

                     Rule:
                        - Use context to generate question 
                        - Do not invent new knowledge
                        - Output valid JSON only
                    """
        return prompt