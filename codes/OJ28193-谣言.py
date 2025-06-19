from collections import defaultdict
def dfs(node):
    status[node] = 1
    ans[-1] = min(ans[-1], c[node])
    for i in e[node]:
        if not status[i]:
            dfs(i)

n, m = map(int, input().split())
e = defaultdict(list)
c = list(map(int, input().split()))
status = [0] * n
ans = []
for i in range(m):
    x, y = map(int, input().split())
    e[x - 1].append(y - 1)
    e[y - 1].append(x - 1)
for i in range(n):
    if not status[i]:
        ans.append(1e9)
        dfs(i)
print(sum(ans))