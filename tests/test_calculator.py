from tools.calculator import calculate

print("=" * 50)
print("Calculator Test")
print("=" * 50)

while True:

    expression = input("\nExpression: ")

    if expression.lower() == "exit":
        break

    result = calculate(expression)

    print("Result:", result)