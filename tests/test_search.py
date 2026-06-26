from tools.search import search_tool

while True:

    query = input("\nSearch: ")

    if query.lower() == "exit":
        break

    results = search_tool.search(query)

    print()

    for result in results:

        print("-" * 50)
        print(result["title"])
        print(result["link"])
        print(result["snippet"])