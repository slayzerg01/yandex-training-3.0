def find_cycle(graph):
    visited = [False] * n
    parent = [-1] * n
    cycle = []

    def dfs(u):
        visited[u] = True
        for v in range(n):
            if graph[u][v]:
                if not visited[v]:
                    parent[v] = u
                    if dfs(v):
                        return True
                elif v != parent[u]:
                    while u != v:
                        cycle.append(u+1)
                        u = parent[u]
                    cycle.append(v+1)
                    return True
        return False

    for u in range(n):
        if not visited[u]:
            if dfs(u):
                cycle.reverse()
                return cycle
    return None


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

cycle = find_cycle(graph)
if cycle:
    print("YES")
    print(len(cycle))
    print(*cycle[::-1])
else:
    print("NO")