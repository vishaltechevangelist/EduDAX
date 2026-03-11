class PromptBuilder:
    def build_mcq_questions(self, chunks, request):
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
    
    def build_subjective_questions(self, chunks, request):
        context = "\n\n".join(chunks)

        instruction = f"Generate {request.num_questions} {request.question_type} questions for class {request.class_name} subject {request.subject} chapter {request.chapter}"

        prompt = f"""Role:  You are CBSE question generator
                     Context: {context}
                     Task: {instruction}

                    Rules:
                        - Questions must test conceptual understanding.
                        - Avoid duplicate or trivial questions.
                        - Questions must strictly come from the provided chapter context.
                        - Use context to generate question 
                        - Do not invent new knowledge
                        - Output valid JSON only

                        Each question must include:
                            - difficulty
                            - marks
                            - question text
                            - expected answer points
                            - rubric for evaluation

                    Rubric must clearly specify how marks are awarded.

                    Output must be STRICT JSON.
                    Do not include explanations outside JSON.

                    JSON format:

                    {{
                            "questions": [
                               {{
                                "id": 1,
                                "question": "Question text",
                                "level": easy | medium | hard,  
                                "expected_answer_points": [],
                                "rubric": [{{"criteria": "", "marks": 1}},
                                           {{"criteria": "", "marks": 1}}],
                                }}
                            ]
                    }}
   
                    """
        return prompt
    
