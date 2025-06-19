from collections import defaultdict
def dfs(node, last):
    if status[node] == 1:
        global loop
        loop = True
        return
    if node in vis or status[node] == 2:
        return
    status[node] = 1
    for i in adj_tab[node]:
        if i != last:
            dfs(i, node)
    status[node] = 2
    vis.add(node)
connect, loop = False, False
n, m = map(int, input().split())
adj_tab = defaultdict(list)
status = [0] * n
for i in range(m):
    u, v = map(int, input().split())
    adj_tab[u].append(v)
    adj_tab[v].append(u)
vis = set()
for i in range(n):
    if i not in vis:
        dfs(i, None)
        if status.count(0) == 0:
            break
if i == 0:
    connect = True
print("connected:", "yes" if connect else "no", sep="")
print("loop:", "yes" if loop else "no", sep="")