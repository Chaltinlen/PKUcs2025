def check(length, n):
    ans = 0
    if length == 0:
        return True
    for i in logs:
        ans += i // length
    return ans >= n

N, K = map(int, input().split())
logs = [int(input()) for i in range(N)]
lo = 0
hi = 10000
mid = 0
while lo < hi:
    mid = (lo + hi) // 2
    if check(mid, K):
        lo = mid + 1
    else:
        hi = mid
print(lo - 1)