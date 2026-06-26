from app.rag import rag

print("=" * 50)
print("AI RAG Assistant")
print("=" * 50)

while True:

    question = input("\nQuestion: ")

    if question.lower() == "exit":
        break

    answer = rag.answer(question)

    print("\nAnswer:\n")

    print(answer)