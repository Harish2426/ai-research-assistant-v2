from app.models import gemini
from app.config import MODEL_NAME

response = gemini.generate(
    "Say hello in one sentence.",
    MODEL_NAME
)

print(response)