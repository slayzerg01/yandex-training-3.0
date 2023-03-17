from sys import setrecursionlimit

setrecursionlimit(10 ** 9)


def dfs(graph, now, col=1):
    global check
    color[now] = col
    for neig in graph[now]:
        if color[neig-1] == 0:
            dfs(graph, neig-1, 3 - color[now])
        elif color[neig-1] == color[now]:
            check = False


with open("input.txt", 'r') as file:
    n, m = map(int, file.readline().split())
    sv = []*n
    for i in range(n):
        sv.append([])
    color = [0] * n
    for i in range(m):
        temp = list(map(int, file.readline().split()))
        if temp[0] != temp[1]:
            sv[temp[0]-1].append(temp[1])
            sv[temp[1]-1].append(temp[0])

check = True
for i in range(n):
    if color[i] == 0:
        dfs(sv, i)
if check:
    print("YES", end='')
else:
    print("NO", end='')