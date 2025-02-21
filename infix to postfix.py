def infix_to_postfix(expression):
    precedence={"+":1,"-":1,"*":2,"/":2,"^":3}
    stack=[]
    output=[]
    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char in precedence:
            while stack and stack[-1]!="(" and precedence[stack[-1]]>=precedence[char]:
                output.append(stack.pop())
            stack.append(char)
        elif char=="(":
            stack.append(char)
        elif char==")":
            while stack and stack[-1]!="(":
                output.append(stack.pop())
            stack.pop()
    while stack:
        output.append(stack.pop())
    return ' '.join(output)

infix="a+b*c/d"
result=infix_to_postfix(infix)
print("the infix_expression is :",infix)
print("the post_fix expression is :",result)





'''def infix_to_postfix(expression):
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}  # Operator precedence
    stack = []  # Stack to hold operators
    output = []  # Output list for the postfix expression
    
    for char in expression:  # Loop through each character in the expression
        if char.isalnum():  # If the character is an operand (A-Z, a-z, 0-9)
            output.append(char)  # Add it to the output list
        elif char in precedence:  # If it's an operator
            while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[char]:
                output.append(stack.pop())  # Pop operators from the stack to the output
            stack.append(char)  # Push the current operator onto the stack
        elif char == '(':
            stack.append(char)  # Push '(' onto the stack
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())  # Pop until '(' is found
            stack.pop()  # Remove '(' from the stack

    # After the expression has been processed, pop all the operators from the stack
    while stack:
        output.append(stack.pop())  # Pop all remaining operators in the stack

    return ''.join(output)  # Join the output list into a string


# Test the function
infix = "a+b*c/d"
result = infix_to_postfix(infix)

print("The infix expression is:", infix)
print("The postfix expression is:", result)'''
