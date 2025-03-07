cnt = 0
def dfs(board, x, y, step, ma):
    if step == ma:
        global cnt
        cnt += 1
        return
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if board[nx][ny] == 0:
            board[nx][ny] = 1
            dfs(board, nx, ny, step+1, ma)
            board[nx][ny] = 0
for i in range(int(input())):
    cnt = 0
    n, m, x, y = map(int, input().split())
    x += 2
    y += 2
    DIRECTIONS = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    board = [[1 for i in range(m+4)] for j in range(2)]+[[1, 1] + [0 for i in range(m)] + [1, 1] for i in range(n)] + [[1 for i in range(m+4)] for j in range(2)]
    board[x][y] = 1
    dfs(board, x, y, 1, m*n)
    print(cnt)