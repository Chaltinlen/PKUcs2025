from collections import deque
DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
def bfs(maze):
    if maze[1][1] == '1' or maze[n][m] == '1':
        return -1
    queue = deque()
    inq = {(1, 1)}
    queue.append((1, 1, 0))
    while queue:
        x, y, step = queue.popleft()
        step += 1
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if (nx, ny) == (n, m):
                return step
            if maze[nx][ny] == '0' and (nx, ny) not in inq:
                queue.append((nx, ny, step))
                inq.add((nx, ny))
    return -1


n, m = map(int, input().split())
maze = [['1' for i in range(m + 2)]] + [['1'] + input().split() + ['1'] for i in range(n)] + [['1' for i in range(m + 2)]]
print(bfs(maze))
