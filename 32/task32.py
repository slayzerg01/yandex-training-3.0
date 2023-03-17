from sys import setrecursionlimit

setrecursionlimit(10 ** 9)


def dfs(graph, visited, now, num_components):
    visited[now] = True
    component[num_components].append(now+1)
    for neig in graph[now]:
        if not visited[neig - 1]:
            dfs(graph, visited, neig - 1, num_components)


with open("input.txt", 'r') as file:
    n, m = map(int, file.readline().split())
    sv = [] * n
    component = []
    num_components = 0
    for i in range(n):
        sv.append([])
        component.append([])

    vs = [False] * n
    for i in range(m):
        temp = list(map(int, file.readline().split()))
        if temp[0] != temp[1]:
            sv[temp[0] - 1].append(temp[1])
            sv[temp[1] - 1].append(temp[0])

for v in range(n):
    if not vs[v]:
        dfs(sv, vs, v, num_components)
        num_components += 1
print(num_components)
for i in range(num_components):
    print(len(component[i]))
    if i < num_components - 1:
        print(*sorted(component[i]))
    else:
        print(*sorted(component[i]), end='')