from math import log2, ceil
N = int(input())
layer = ceil(log2(N + 1)) - 1
treasure = list(map(int, input().split()))
dp = [[0 for i in range(2**(layer+1))] for j in range(2)]
for i in range(2**layer - 1, N):
    dp[1][i] = treasure[i]
    dp[0][i] = 0
for i in range(2**layer - 2, -1, -1):
    dp[0][i] = max(dp[0][2*i+1], dp[1][2*i+1]) + max(dp[0][2*i+2], dp[1][2*i+2])
    dp[1][i] = treasure[i] + dp[0][2 * i + 1] + dp[0][2 * i + 2]
print(max(dp[0][0], dp[1][0]))