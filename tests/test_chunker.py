from tools.pdf_reader import pdf_reader
from tools.chunker import chunker

text = pdf_reader.read("uploads/resume.pdf")

chunks = chunker.split(text)

print(f"Total Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i+1}")
    print("-" * 50)
    print(chunk[:300])