from google import genai
from google.genai import errors
from app.config import GEMINI_API_KEY
import time


class GeminiClient:
    def __init__(self):

        if not GEMINI_API_KEY:
            raise ValueError(
                "❌ GEMINI_API_KEY not found.\n"
                "Add it to your .env file (local) or Streamlit Secrets (cloud)."
            )

        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    def generate(self, prompt, model_name):

        for attempt in range(3):

            try:

                response = self.client.models.generate_content(
                    model=model_name,
                    contents=prompt
                )

                return response.text

            except errors.ServerError:
                if attempt < 2:
                    time.sleep(2)
                    continue

                return (
                    "⚠️ Gemini server is currently busy (503).\n"
                    "Please try again in a few seconds."
                )

            except errors.ClientError as e:
                return f"❌ Client Error: {e}"

            except Exception as e:
                return f"❌ Error: {e}"


gemini = GeminiClient()