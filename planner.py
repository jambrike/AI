import json
from llm.gemini_client import GeminiClient

class Planner:
    def __init__(self):
        self.client = GeminiClient()

    def create_plan(self, instruction: str):
        prompt = f"""
You are an autonomous AI kernel planner.
Break down this instruction into JSON steps.
Instruction: {instruction}
Output as JSON array: [{{"action":"...","args":{{}}}}]
"""
        response = self.client.chat(prompt)
        return json.loads(response)
