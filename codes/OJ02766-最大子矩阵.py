# TODO
from pprint import pprint
N = int(input())
nums = list(map(int, input().split()))
matrix = [[0] * (N + 1)] + [[0] + [nums[i * N + j] for j in range(N)] for i in range(N)]
col_pref = [[0 for j in range(N + 1)] for i in range(N + 1)]
row_pref = [[0 for j in range(N + 1)] for i in range(N + 1)]
col_maxsub = [[(0, 0)] * (N + 1)] + [[(0, i + 1)] + [(nums[i * N + j], i + 1) for j in range(N)] for i in range(N)]
row_maxsub = [[(0, i) for i in range(N + 1)]] + [[(0, 0)] + [(nums[i * N + j], j + 1) for j in range(N)] for i in range(N)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        col_pref[i][j] = matrix[i][j] + col_pref[i - 1][j]
        row_pref[i][j] = matrix[i][j] + row_pref[i][j - 1]
        if col_maxsub[i - 1][j][0] > 0:
        col_maxsub[i][j] = (max(matrix[i][j], col_maxsub[i - 1][j][0] + matrix[i][j]), i)
        row_maxsub[i][j] = (max(matrix[i][j], row_maxsub[i][j - 1][0] + matrix[i][j]), j)
pprint(col_maxsub)

# dp = [[[0, i, j] for j in range(N + 1)] for i in range(N + 1)]
# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         dp[i][]

