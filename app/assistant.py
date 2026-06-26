from app.router import router
from app.models import gemini
from app.config import MODEL_NAME

from app.rag import rag
from tools.calculator import calculate
from tools.search import search_tool


class Assistant:

    def get_response(self, question):

        tool = router.route(question)

        print(f"Selected Tool: {tool}")

        # Calculator
        if tool == "calculator":

            result = calculate(question)

            prompt = f"""
User Question:
{question}

Calculator Result:
{result}

Explain the result clearly.
"""

            return gemini.generate(prompt, MODEL_NAME)

        # Search
        elif tool == "search":

            results = search_tool.search(question)

            prompt = f"""
Search Results:

{results}

User Question:

{question}

Provide a concise answer.
"""

            return gemini.generate(prompt, MODEL_NAME)

        # RAG
        elif tool == "rag":

            return rag.answer(question)

        # Normal Chat
        else:

            return gemini.generate(question, MODEL_NAME)


assistant = Assistant()