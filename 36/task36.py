from collections import deque


def bfs_shortest_path(adj_matrix, src, dest):
    dist = [float('inf')] * n
    dist[src] = 0

    q = deque()
    q.append(src)

    while q:
        curr = q.popleft()

        if curr == dest:
            return dist[dest]

        for neighbor in range(n):
            if adj_matrix[curr][neighbor] and dist[neighbor] == float('inf'):
                dist[neighbor] = dist[curr] + 1
                q.append(neighbor)

    return -1


n = int(input())
matrix = [tuple(map(int, input().split())) for _ in range(n)]
src, dest = map(int, input().split())
print(bfs_shortest_path(matrix, src-1, dest-1))