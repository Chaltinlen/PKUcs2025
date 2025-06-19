from sys import stdin
readin = map(int, stdin.read().split())
N = next(readin)
M = next(readin)
hashtable = [0] * M
pos = [0] * N
nums = []
for i in range(N):
    nums.append(next(readin))
for i in range(N):
    j = 0
    h = nums[i] % M
    p = h
    while hashtable[p] and hashtable[p] != nums[i]:
        p = (h + (-1 if j % 2 else 1) * (j // 2 + 1)**2) % M
        j += 1
    pos[i] = p
    hashtable[p] = nums[i]
print(*pos)