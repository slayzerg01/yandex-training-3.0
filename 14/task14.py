from collections import deque

with open('input.txt', 'r') as file:
    n = int(file.readline())
    text = file.readline().split()
    stack = deque()
    out = []
    for value in text:
        stack.append(int(value))
        while True:
            if len(out) != 0:
                try:
                    if stack[-1] == out[-1] + 1:
                        out.append(stack.pop())
                    else:
                        break
                except IndexError:
                    break
            else:
                if stack[-1] == 1:
                    out.append(stack.pop())
                else:
                    break

    while len(stack) != 0:
        out.append(stack.pop())

if out == sorted(out):
    print("YES", end='')
else:
    print("NO", end='')