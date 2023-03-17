from collections import deque

with open('input.txt', 'r') as file:
    n = int(file.readline())
    text = [list(tup) for tup in zip(list(map(int, file.readline().split())), [i for i in range(n)], [-1 for i in range(n)])]
    stack = deque()
    stack.append(text[0])
    for i in range(1, n + 1):
        if i != n:
            new_elem = text[i]
            try:
            	while stack[-1][0] > new_elem[0]:
                    text[stack[-1][1]][2] = new_elem[1]
                    deleted = stack.pop()
            except IndexError:
                continue
            finally:
            	stack.append(new_elem)

for i in range(n):
    print(text[i][2], end=' ')