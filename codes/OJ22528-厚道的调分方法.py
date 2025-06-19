from math import pow
scores = sorted(map(float, input().split()))
stu = scores[len(scores) * 2 // 5]
lo, hi = 0, int(1e9)
while lo < hi:
    mid = (lo + hi) // 2
    ax = mid / 1e9 * stu
    if ax + pow(1.1, ax) < 85:
        lo = mid + 1
    else:
        hi = mid
print(lo)