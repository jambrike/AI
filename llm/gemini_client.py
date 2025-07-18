import os
import subprocess
import json

class GeminiClient:
    def __init__(self):
        self.token = os.getenv("GEMINI_AUTH_TOKEN")
        if not self.token:
            raise EnvironmentError("GEMINI_AUTH_TOKEN not set")

    def chat(self, prompt: str) -> str:
        # Run Gemini CLI with prompt and token
        proc = subprocess.run(
            ["gemini", "chat", "--json", prompt],
            capture_output=True,
            text=True,
            env={**os.environ, "GEMINI_AUTH_TOKEN": self.token}
        )
        if proc.returncode != 0:
            raise RuntimeError(f"Gemini CLI failed: {proc.stderr}")
        response_json = json.loads(proc.stdout)
        return response_json.get("response", "")
