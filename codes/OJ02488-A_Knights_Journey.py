from collections import deque
from math import ceil
DIRECTIONS = ((-1, -2), (1, -2), (-2, -1), (2, -1), (-2, 1), (2, 1), (-1, 2), (1, 2))
ans = "impossible"
class Found(Exception):
    pass


def check(coors):
    global ans
    ans = ""
    for i, j in coors:
        ans += chr(65 + j) + str(i + 1)
def dfs(x, y, path):
    # print(x, y, path)
    global p, q
    if len(path) == p * q:
        check(path)
        raise Found
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < p and 0 <= ny < q and not board[nx][ny]:
            board[nx][ny] = 1
            dfs(nx, ny, path + [(nx, ny)])
            board[nx][ny] = 0


for i in range(1, 1 + int(input())):
    ans = "impossible"
    p, q = map(int, input().split())
    board = [[0 for i in range(q)] for j in range(p)]
    board[0][0] = 1
    try:
        dfs(0, 0, [(0, 0)])
    except Found:
        pass
    print(f"Scenario #{i}:\n" + ans + "\n")
