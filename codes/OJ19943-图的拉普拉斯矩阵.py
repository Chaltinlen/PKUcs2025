class Vertex:
    def __init__(self, n, D=[[]]):
        self.D = D
        for i in range(n):
            for j in range(n):
                D[-1].append(0)
            D.append([])
class Graph:
    def __init__(self, n, A=[[]]):
        self.A = A
        for i in range(n):
            for j in range(n):
                A[-1].append(0)
            A.append([])

n, m = map(int, input().split())
v = [Vertex(n)] * n
G = Graph(n)
ans = [[0 for j in range(n)] for i in range(n)]
for i in range(m):
    v1, v2 = map(int, input().split())
    v[v1].D[v1][v1] += 1
    v[v2].D[v2][v2] += 1
    G.A[v1][v2] = G.A[v2][v1] = 1
for i in range(n):
    for j in range(n):
        ans[i][j] = v[0].D[i][j] - G.A[i][j]
    print(*ans[i])
