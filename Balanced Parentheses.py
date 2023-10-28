def are_pair(open, close):
    if open == '(' and close == ')':
        return True
    elif open == '{' and close == '}':
        return True
    elif open == '[' and close == ']':
        return True
    return False

def are_balanced(exp):
    stack = []
    length = len(exp)
    for i in range(length):
        if exp[i] == '(' or exp[i] == '{' or exp[i] == '[':
            stack.append(exp[i])
        elif exp[i] == ')' or exp[i] == '}' or exp[i] == ']':
            if not stack or not are_pair(stack[-1], exp[i]):
                return False
            else:
                stack.pop()
    return not stack

if __name__ == "__main__":
    expression = input("Enter an expression: ")
    if are_balanced(expression):
        print("Balanced")
    else:
        print("Not Balanced")
