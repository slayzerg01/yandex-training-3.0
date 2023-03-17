from collections import deque

with open('input.txt', 'r') as file:
    line1 = list(map(int, file.readline().split()))
    line2 = list(map(int, file.readline().split()))
    op1 = deque()
    op2 = deque()
    for i in range(len(line1)):
        op1.append(line1[i])
        op2.append(line2[i])
    index = 0
    while len(op1) != 0 and len(op2) != 0:
        a = op1.popleft()
        b = op2.popleft()
        if a > b:
            if b == 0 and a == 9:
                op2.append(a)
                op2.append(b)
            else:
                op1.append(a)
                op1.append(b)
        else:
            if a == 0 and b == 9:
                op1.append(a)
                op1.append(b)
            else:
                op2.append(a)
                op2.append(b)
        index += 1

if len(op2) == 0:
    print(f"first {index}")
else:
    print(f"second {index}")