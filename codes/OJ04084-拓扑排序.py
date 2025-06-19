from heapq import heappush, heappop
class Vertex:
    def __init__(self, n):
        self.num = n
        self.name = f"v{n + 1}"
        self.ind = 0
v, a = map(int, input().split())
ans = []
heap = []
adj_mat = [[False for i in range(v)] for j in range(v)]
nodes = [Vertex(i) for i in range(v)]
for i in range(a):
    n1, n2 = map(int, input().split())
    if not adj_mat[n1 - 1][n2 - 1]:
        nodes[n2 - 1].ind += 1
        adj_mat[n1 - 1][n2 - 1] = True
for i in nodes:
    if not i.ind:
        heappush(heap, i.num)
while heap:
    node = heappop(heap)
    for i in range(v):
        if adj_mat[node][i]:
            nodes[i].ind -= 1
            if nodes[i].ind == 0:
                heappush(heap, i)
    ans.append(nodes[node].name)

print(*ans)