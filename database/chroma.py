import chromadb

from tools.embeddings import embedding_model


class ChromaDatabase:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="database/chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

    def add_chunks(self, chunks):

        for i, chunk in enumerate(chunks):

            embedding = embedding_model.encode(chunk)

            self.collection.add(

                ids=[str(i)],

                embeddings=[embedding.tolist()],

                documents=[chunk]

            )

    def search(self, question, n_results=3):

        query_embedding = embedding_model.encode(question)

        results = self.collection.query(

            query_embeddings=[query_embedding.tolist()],

            n_results=n_results

        )

        return results["documents"][0]


db = ChromaDatabase()