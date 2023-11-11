def is_operator(ch):
    return ch in {'+', '-', '*', '/'}


def perform_operation(op1, op2, op):
    if op == '+':
        return op2 + op1
    elif op == '-':
        return op2 - op1
    elif op == '*':
        return op2 * op1
    elif op == '/':
        return op2 / op1


def evaluate_postfix(expression):
    stack = []
    operators = {'+', '-', '*', '/'}

    tokens = expression.split()

    for token in tokens:
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            stack.append(int(token))
        elif token in operators:
            op1 = stack.pop()
            op2 = stack.pop()
            result = perform_operation(op1, op2, token)
            stack.append(result)

    return stack.pop()


if __name__ == "__main__":
    expression = input("Enter a Postfix Expression (e.g., 4 5 *):\n")
    result = evaluate_postfix(expression)
    print("Answer =", result)
