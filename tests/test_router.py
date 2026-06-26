from app.router import router

print("=" * 50)
print("AI Router Test")
print("=" * 50)

while True:

    question = input("\nQuestion: ")

    tool = router.route(question)

    if tool == "exit":
        print("Goodbye!")
        break

    print(f"Selected Tool: {tool}")