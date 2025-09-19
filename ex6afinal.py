def infix_to_postfix(expression):
    precedence = {"(": 0, "+" : 1, "-" : 1, "*" : 2, "/" : 2}
    output = []
    stack = []

    for char in expression:
        if char.isalnum():  # Operand
            output.append(char)
        elif char == "(":   # Left parenthesis
            stack.append(char)
        elif char == ")":   # Right parenthesis
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()  # Remove '(' from stack
        else:  # Operator
            while stack and precedence[char] <= precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(char)

    # Pop remaining operators from the stack
    while stack:
        output.append(stack.pop())

    return "".join(output)

exp = input("Enter infix expression: ")
postfix = infix_to_postfix(exp)
print("Postfix expression:", postfix)
