from google import genai
from app.config import GEMINI_API_KEY


class GeminiClient:

    def __init__(self):

        if not GEMINI_API_KEY:
            raise ValueError(
                "GEMINI_API_KEY not found. Add it to .env or Streamlit Secrets."
            )

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    def generate(self, prompt, model_name):

        try:

            response = self.client.models.generate_content(
                model=model_name,
                contents=prompt
            )

            return response.text

        except Exception as e:

            return f"Error: {e}"


gemini = GeminiClient()