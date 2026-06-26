from google import genai
from google.genai import errors
from app.config import GEMINI_API_KEY


class GeminiClient:

    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def generate(self, prompt, model_name):

        try:

            response = self.client.models.generate_content(
                model=model_name,
                contents=prompt
            )

            return response.text

        except errors.ServerError:
            return (
                "⚠️ Gemini server is currently busy (503).\n"
                "Please try again in a few seconds."
            )

        except Exception as e:
            return f"Error: {e}"


gemini = GeminiClient()