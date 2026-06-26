import ast
import operator

# Allowed operators
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
}


def evaluate(node):
    """Recursively evaluate AST nodes."""

    if isinstance(node, ast.Constant):
        return node.value

    elif isinstance(node, ast.BinOp):

        left = evaluate(node.left)
        right = evaluate(node.right)

        return OPERATORS[type(node.op)](left, right)

    elif isinstance(node, ast.UnaryOp):

        operand = evaluate(node.operand)

        return OPERATORS[type(node.op)](operand)

    raise TypeError("Unsupported expression")


def calculate(expression: str):
    """
    Safely evaluate a mathematical expression.
    """

    try:

        tree = ast.parse(expression, mode="eval")

        return evaluate(tree.body)

    except Exception as e:

        return f"Calculation Error: {e}"