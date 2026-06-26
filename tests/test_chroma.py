from tools.pdf_reader import pdf_reader
from tools.chunker import chunker

from database.chroma import db

print("Reading PDF...")

text = pdf_reader.read("uploads/resume.pdf")

print("Chunking...")

chunks = chunker.split(text)

print("Saving to ChromaDB...")

db.add_chunks(chunks)

print("Done!")

print()

question = input("Question: ")

results = db.search(question)

print()

print("=" * 60)

for chunk in results:

    print(chunk)

    print("-" * 60)