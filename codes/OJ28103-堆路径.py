def dfs(node, prev):
    global n
    if 2 * node + 2 < n:
        dfs(2 * node + 2, prev + [tree[node]])
    if 2 * node + 1 < n:
        dfs(2 * node + 1, prev + [tree[node]])
    else:
        seq.append(prev + [tree[node]])
seq = []
n = int(input())
tree = list(map(int, input().split()))
t = [0 for i in range(3)]
dfs(0, [])
for i in seq:
    print(*i)
    si = sorted(i)
    if i == si:
        t[0] += 1
    elif i == si[::-1]:
        t[1] += 1
    else:
        t[2] += 1
if t[2]:
    print("Not Heap")
else:
    if not t[1]:
        print("Min Heap")
    elif not t[0]:
        print("Max Heap")
    else:
        print("Not Heap")