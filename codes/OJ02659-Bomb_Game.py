from math import dist
A, B, K = map(int, input().split())
board = [[1 for i in range(B)] for j in range(A)]
for i in range(K):
    R, S, P, T = map(int, input().split())
    for x in range(A):
        for y in range(B):
            if abs(x - R + 1) <= P // 2 and abs(y - S + 1) <= P // 2:
                board[x][y] &= T
            else:
                board[x][y] &= 1 - T
print(sum(map(sum, board)))