def ispossible(dis):
    cnt = 0
    last = 0
    for rock in rocks:
        if rock - last < dis:
            cnt += 1
        else:
            last = rock
    return cnt <= M
L, N, M = map(int, input().split())
rocks = [int(input()) for i in range(N)] + [L]
lo = 0
hi = L
while lo < hi:
    mid = (lo + hi) // 2
    if ispossible(mid):
        lo = mid + 1
    else:
        hi = mid
print(lo - 1)
