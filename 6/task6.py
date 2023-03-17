col = []
with open('input.txt', 'r') as file:
    n = int(file.readline())
    for i in range(n):
        col.append(int(file.readline()))
sum = 0
for i in range(n-1):
    if col[i] >= col[i+1]:
        sum += col[i+1]
    else:
        sum += col[i]
print(sum)
