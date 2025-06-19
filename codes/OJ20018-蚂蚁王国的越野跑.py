from bisect import bisect_right
from random import randint
inv = 0
def MergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = MergeSort(arr[:mid])
    right = MergeSort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    global inv
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            inv += len(left) - i
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ans1, ans2 = 0, 0
# while ans1 == ans2:
#     ans1, ans2 = 0, 0
#     N = 5
#     v = [randint(1, N) for i in range(N)]
#     print(*v, sep=" ")
#     surpass = [9 for i in range(N + 1)]
#     for ant in v:
#         surpass[bisect_right(surpass, ant)] = ant
#         ans1 += bisect_right(surpass, ant - 1)

#     MergeSort(v)
#     ans2 = inv
#     print(surpass, ans1, ans2)


N = int(input())
v = [int(input()) for i in range(N)]
MergeSort(v)
print(inv)