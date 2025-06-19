change = 0
def merge(arr1, arr2):
    global change
    ans = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            change += len(arr1) - i
            j += 1
    ans += arr1[i:]
    ans += arr2[j:]
    return ans
def MergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left = MergeSort(arr[:mid])
        right = MergeSort(arr[mid:])
        return merge(left, right)
while True:
    change = 0
    n = int(input())
    if n == 0:
        break
    arr = [int(input()) for i in range(n)]
    a = MergeSort(arr)
    print(change)