def infix_to_postfix(expression):
    stack = []
    postfix = ""

    def is_operator(char):
        return char in {'+', '-', '*', '/', '$'}

    def has_higher_precedence(operator1, operator2):
        weight1 = get_operator_weight(operator1)
        weight2 = get_operator_weight(operator2)

        if weight1 == weight2:
            return not is_right_associative(operator1)
        return weight1 > weight2

    def is_right_associative(op):
        return op == '$'

    def get_operator_weight(op):
        weights = {'+': 1, '-': 1, '*': 2, '/': 2, '$': 3}
        return weights[op] if op in weights else -1

    for char in expression:
        if char == ' ' or char == ',':
            continue
        elif is_operator(char):
            while stack and stack[-1] != '(' and has_higher_precedence(stack[-1], char):
                postfix += stack.pop()
            stack.append(char)
        elif char.isalnum():
            postfix += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()

    while stack:
        postfix += stack.pop()

    return postfix


if __name__ == "__main__":
    expression = input("Enter Infix Expression:\n")
    result = infix_to_postfix(expression)
    print("Output =", result)
