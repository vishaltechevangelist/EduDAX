import requests

class OllamaClient:
    def generate(self, prompt):
        # print(prompt)
        response = requests.post(url="http://localhost:11434/api/generate", json={
                                                                            'model':"llama3",
                                                                            'prompt': prompt,
                                                                            'stream': False,
                                                                            'format':"json"
                                                                            })
        response.raise_for_status()
        # print(response.json())
        return response.json()['response']