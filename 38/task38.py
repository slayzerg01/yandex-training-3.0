from queue import Queue


def bfs(start):
    distances = [[-1] * m for _ in range(n)]
    q = Queue()
    q.put(start)
    distances[start[0]][start[1]] = 0

    while not q.empty():
        curr = q.get()
        for move in [(1, 2), (2, 1), (-1, -2), (-2, -1), (1, -2), (-1, 2), (-2, 1), (2, -1)]:
            neighbor = (curr[0] + move[0], curr[1] + move[1])
            if 0 <= neighbor[0] < n and 0 <= neighbor[1] < m and distances[neighbor[0]][neighbor[1]] == -1:
                distances[neighbor[0]][neighbor[1]] = distances[curr[0]][curr[1]] + 1
                q.put(neighbor)

    return distances


n, m, s, t, q = map(int, input().split())
s -= 1
t -= 1
board = [[False] * m for _ in range(n)]
board[s][t] = True

for i in range(q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    board[x][y] = True

distances = bfs((s, t))
if distances == -1:
    print(-1)
else:
    total_distance = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] and distances[i][j] == -1:
                print(-1)
                exit()
            if board[i][j]:
                total_distance += distances[i][j]
    print(total_distance)