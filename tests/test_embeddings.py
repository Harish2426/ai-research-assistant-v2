from tools.embeddings import embedding_model

text = "Python is one of my programming skills."

embedding = embedding_model.encode(text)

print("=" * 50)
print("Embedding Length:", len(embedding))
print("=" * 50)

print(embedding[:10])