from sys import setrecursionlimit

setrecursionlimit(10 ** 9)


def dfs(graph, now):
    global check
    color[now] = 1
    for neig in graph[now]:
        if color[neig-1] == 0:
            dfs(graph, neig-1)
        elif color[neig-1] == 1:
            color[now] = 2
            check = False
    color[now] = 2
    path.append(now+1)

check = True
with open("input.txt", 'r') as file:
    n, m = map(int, file.readline().split())
    sv = []*n
    edges = []
    for i in range(n):
        sv.append([])
    color = [0] * n
    for i in range(m):
        temp = list(map(int, file.readline().split()))
        edges.append(tuple(temp))
        if temp[0] != temp[1]:
            sv[temp[0]-1].append(temp[1])
        if temp[0] == temp[1]:
            check = False

path = []
if check:
    check = True
    for i in range(n):
        if color[i] == 0:
            dfs(sv, i)
    if check:
        print(*path[::-1], end='')
    else:
        print('-1', end='')
else:
    print('-1', end='')