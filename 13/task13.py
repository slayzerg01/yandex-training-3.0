from collections import deque

with open('input.txt', 'r') as file:
    text = file.readline().split()
    stack = deque()
    for symbol in text:
        if symbol.isnumeric():
            stack.append(int(symbol))
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            if symbol == '-':
                stack.append(op2 - op1)
            elif symbol == '+':
                stack.append(op1 + op2)
            elif symbol == '*':
                stack.append(op1*op2)
print(stack.pop(), end='')