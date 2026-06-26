from database.chroma import db


class RAGService:

    def answer(self, question):

        chunks = db.search(question)

        if not chunks:
            return "No matching chunks found."

        context = "\n\n".join(chunks)

        return f"""
=========================
RETRIEVED CONTEXT
=========================

{context}

=========================
RAG Retrieval Successful ✅
Gemini API call skipped.
"""


rag = RAGService()