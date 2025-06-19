from collections import defaultdict
def dfs(node, last):
    if node in restr or node in vis:
        return
    for i in e[node]:
        if i != last:
            dfs(i, node)
    vis.add(node)
n = int(input())
e = defaultdict(list)
for i in range(n - 1):
    u, v = map(int, input().split())
    e[u].append(v)
    e[v].append(u)
restr = set(map(int, input().split()))
vis = set()
dfs(0, None)
print(len(vis))