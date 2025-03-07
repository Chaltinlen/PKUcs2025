def ispossible(mid):
    global N, M
    cnt = 0
    m = 0
    for c in cost:
        if c > mid: 
            return False
        m += c
        if m > mid:
            cnt += 1
            m = c
    return cnt + 1 <= M
N, M = map(int, input().split())
cost = [int(input()) for i in range(N)]
lo = 1
hi = sum(cost)
while lo < hi:
    mid = (hi + lo) // 2
    if ispossible(mid):
        hi = mid
    else:
        lo = mid + 1
print(lo)
