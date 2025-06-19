abs_diff = diff = min_diff = min_abs_diff = 1e9
T = int(input())
S = sorted(map(int, input().split()))
i, j = 0, len(S) - 1
while i < j:
    diff = S[i] + S[j] - T
    abs_diff = abs(diff)
    if (abs_diff, diff) < (min_abs_diff, min_diff):
        min_diff = diff
        min_abs_diff = abs_diff
    else:
        if diff > 0:
            j -= 1
        elif diff < 0:
            i += 1
        else:
            break
print(T + min_diff)