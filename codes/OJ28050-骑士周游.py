DIRECTIONS = ((1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1))
def calc_adj(t):
    global n
    cnt = 0
    for dx, dy in DIRECTIONS:
        if 0 <= t[0] + dx < n and 0 <= t[1] + dy < n and not board[t[0] + dx][t[1] + dy]:
            cnt += 1
    return cnt
def dfs(x, y, depth):
    board[x][y] = 1
    if depth == n * n:
        exit()
    nxt = [(x + dx, y + dy) for dx, dy in DIRECTIONS if 0 <= x + dx < n and 0 <= y + dy < n and not board[x + dx][y + dy]]
    for nx, ny in sorted(nxt, key=calc_adj):
        dfs(nx, ny, depth + 1)
    board[x][y] = 0


n = int(input())
board = [[0 for i in range(n)] for j in range(n)]
sr, sc = map(int, input().split())
board[sr][sc] = 1
try:
    dfs(sr, sc, 1)
except SystemExit:
    print("success")
else:
    print("fail")
