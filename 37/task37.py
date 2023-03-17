import heapq


def dijkstra_shortest_path(adj_matrix, src, dest):
    dist = [float('inf')] * n
    dist[src] = 0
    parent = [None] * n

    pq = []
    heapq.heappush(pq, (0, src))

    while pq:
        curr_dist, curr = heapq.heappop(pq)

        if curr == dest:
            path = []
            while curr is not None:
                path.append(curr+1)
                curr = parent[curr]
            path.reverse()
            return dist[dest], path

        for neighbor in range(n):
            weight = adj_matrix[curr][neighbor]
            if weight != 0:
                new_dist = dist[curr] + weight
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    parent[neighbor] = curr
                    heapq.heappush(pq, (new_dist, neighbor))

    return -1, []


n = int(input())
matrix = [tuple(map(int, input().split())) for _ in range(n)]
src, dest = map(int, input().split())
if src != dest:
    l, path = dijkstra_shortest_path(matrix, src-1, dest-1)
    print(l)
    print(*path)
else:
    print(0)
    print(' ', end='')