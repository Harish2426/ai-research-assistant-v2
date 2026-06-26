from app.models import gemini
from app.config import MODEL_NAME


class AIRouter:

    def route(self, question: str) -> str:

        question_lower = question.lower()

        # =====================================
        # Rule-Based Routing (Fast)
        # =====================================

        # Calculator
        if any(op in question for op in ["+", "-", "*", "/", "%"]):
            return "calculator"

        # Search
        if any(word in question_lower for word in [
            "latest",
            "news",
            "today",
            "recent",
            "current",
            "search",
            "find on internet",
            "web"
        ]):
            return "search"

        # RAG
        if any(word in question_lower for word in [
            "resume",
            "cv",
            "project",
            "projects",
            "skill",
            "skills",
            "education",
            "experience",
            "certificate",
            "certificates",
            "document",
            "pdf",
            "file",
            "uploaded"
        ]):
            return "rag"

        # Exit
        if question_lower in ["exit", "quit", "bye"]:
            return "exit"

        # =====================================
        # AI Router (Fallback)
        # =====================================

        prompt = f"""
You are an AI Tool Router.

Choose ONLY ONE tool.

Available tools:

calculator
- Math calculations.

search
- Latest news, internet information, current events.

rag
- Questions about uploaded documents, PDFs, resumes, projects, education, skills or experience.

chat
- Everything else.

Question:
{question}

Return ONLY ONE WORD.

Allowed answers:

calculator
search
rag
chat
"""

        try:

            tool = gemini.generate(
                prompt,
                MODEL_NAME
            )

            tool = tool.strip().lower()

            allowed = [
                "calculator",
                "search",
                "rag",
                "chat"
            ]

            if tool in allowed:
                return tool

            return "chat"

        except Exception:

            return "chat"


router = AIRouter()