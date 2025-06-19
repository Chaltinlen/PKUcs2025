def dfs(node):
    colour[node] = 1
    for nv in filter(lambda i: adj_mat[node][i], range(n)):
        if not colour[nv]:
            dfs(nv)
        elif colour[nv] == 1:
            exit()
    colour[node] = 2
n, m = map(int, input().split())
adj_mat = [[False for i in range(n)] for j in range(n)]
edge_cnt = [0] * n
for i in range(m):
    u, v = map(int, input().split())
    adj_mat[u][v] = True
    edge_cnt[u] += 1
colour = [0] * n
try:
    for i in range(n):
        if not colour[i]:
            dfs(i)
except SystemExit:
    print("Yes")
else:
    print("No")