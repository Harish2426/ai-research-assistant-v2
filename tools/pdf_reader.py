from pypdf import PdfReader
import os


class PDFReader:

    def read(self, file_path):

        # Remove quotes if user pasted them
        file_path = file_path.strip().strip('"').strip("'")

        # Normalize path
        file_path = os.path.normpath(file_path)

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text


pdf_reader = PDFReader()