from tools.pdf_reader import pdf_reader

path = input("PDF Path: ")

text = pdf_reader.read(path)

print("\n")

print(text[:2000])