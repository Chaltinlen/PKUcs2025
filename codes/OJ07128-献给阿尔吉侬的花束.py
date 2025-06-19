DIRECTIONS = ((0, 1), (1, 0), (0, -1), (-1, 0))
from collections import deque
for i in range(int(input())):
    R, C = map(int, input().split())
    board = [input() for i in range(R)]
    queue = deque()
    for i in range(R):
        if "S" in board[i]:
            queue.append((i, board[i].index("S"), 0))
            break
    inq = {(queue[0][0], queue[0][1])}
    while queue:
        x, y, step = queue.popleft()
        if board[x][y] == "E":
            print(step)
            break
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != "#" and (nx, ny) not in inq:
                queue.append((nx, ny, step + 1))
                inq.add((nx, ny))
    else:
        print("oop!")
