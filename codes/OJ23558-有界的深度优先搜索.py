ans = []
def dfs(node, pref, L):
    ans.append(node)
    status[node] = True
    if len(pref) == L:
        return
    for i in range(n):
        if e[node][i] and not status[i]:
            dfs(i, pref + [i], L)

n, m, L = map(int, input().split())
e = [[False for i in range(n)] for j in range(n)]
for i in range(m):
    n1, n2 = map(int, input().split())
    e[n1][n2] = e[n2][n1] = True
status = [False] * n
start = int(input())
status[start] = True
dfs(start, [], L)

print(*ans)
