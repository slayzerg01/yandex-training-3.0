from sys import setrecursionlimit
setrecursionlimit(10**9)


def dfs(graph, visited, now):
    visited[now] = True
    for neig in graph[now]:
        if not visited[neig-1]:
            dfs(graph, visited, neig-1)


with open("input.txt", 'r') as file:
    n, m = map(int, file.readline().split())
    sv = []*n
    for i in range(n):
        sv.append([])
    vs = [False] * n
    for i in range(m):
        temp = list(map(int, file.readline().split()))
        if temp[0] != temp[1]:
            sv[temp[0]-1].append(temp[1])
            sv[temp[1]-1].append(temp[0])

dfs(sv, vs, 0)
print(vs.count(True))
for i in range(n):
    if vs[i]:
        print(i + 1, end=' ')