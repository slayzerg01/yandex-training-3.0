from collections import deque


def solve():
    n = int(input())
    cave = []
    for _ in range(n):
        input()
        level = []
        for _ in range(n):
            line = input().strip()
            level.append(list(line))
            if 'S' in line:
                start = (len(cave), len(level) - 1, line.index('S'))
        cave.append(level)

    queue = deque([(start, 0)])
    visited = set([start])
    while queue:
        node, dist = queue.popleft()
        if node[0] == 0:
            return dist
        for dx, dy, dz in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
            nx, ny, nz = node[0] + dx, node[1] + dy, node[2] + dz
            if nx < 0 or nx >= n or ny < 0 or ny >= n or nz < 0 or nz >= n:
                continue
            if cave[nx][ny][nz] == '#' or (nx, ny, nz) in visited:
                continue
            queue.append(((nx, ny, nz), dist + 1))
            visited.add((nx, ny, nz))

    return -1


print(solve())