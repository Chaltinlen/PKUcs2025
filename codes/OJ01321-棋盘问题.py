cnt = 0
def num_count(piece, depth, pos_col):
    global cnt
    if k - piece > n - depth:
        return
    if k == piece:
        cnt += 1
        return
    for i in pos_col:
        if board[depth][i] == "#":
            num_count(piece + 1, depth + 1, pos_col - {i})
    num_count(piece, depth + 1, pos_col)


while True:
    n, k = map(int, input().split())
    if n == -1:
        break
    col = set(range(n))
    board = [list(input()) for i in range(n)]
    cnt = 0
    num_count(0, 0, col)
    print(cnt)
