from collections import deque

with open('input.txt', 'r') as file:
    text = file.read().replace('\n', '')
    stack = deque()
    check = True
    for symbol in text:
        if symbol == '(' or symbol == '[' or symbol == '{':
            stack.append(symbol)
        else:
            try:
                temp = stack.pop()
                if symbol == ')' and temp != '(':
                    check = False
                    break
                elif symbol == ']' and temp != '[':
                    check = False
                    break
                elif symbol == '}' and temp != '{':
                    check = False
                    break
            except IndexError:
                check = False
                break
    if check and len(stack) == 0:
        print('yes', end='')
    else:
        print('no', end='')