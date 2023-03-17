matr = []
with open('input.txt', 'r') as file:
    m = int(file.readline())
    n = int(file.readline())
    for i in range(n):
        matr.append(list(map(int, file.readline().split())))
i = 1
while i <= n-1:
    j = 0
    while j < i:
        if not(matr[i][0] > matr[j][1] or matr[i][1] < matr[j][0]):
            matr.remove(matr[j])
            n -= 1
            i -= 1
            j -= 1
        j += 1
    i += 1
print(len(matr))