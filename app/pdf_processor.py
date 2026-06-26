import os

from tools.pdf_reader import pdf_reader
from tools.chunker import chunker
from database.chroma import db


class PDFProcessor:

    def process(self, uploaded_file):

        os.makedirs("uploads", exist_ok=True)

        file_path = os.path.join(
            "uploads",
            uploaded_file.name
        )

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        text = pdf_reader.read(file_path)

        chunks = chunker.split(text)

        db.add_chunks(chunks)

        return len(chunks)


pdf_processor = PDFProcessor()