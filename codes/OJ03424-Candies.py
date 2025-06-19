from heapq import heappush, heappop
N, M = map(int, input().split())
adj_mat = [[] for j in range(N)]
heap = []
for i in range(M):
    a, b, c = map(int, input().split())
    adj_mat[a-1].append((b-1, c))
dist = [1e11 for i in range(N)]
heap = [(0, 0)]
while heap:
    d, node = heappop(heap)
    if node == N - 1:
        dist[-1] = d
        break
    for i, w in adj_mat[node]:
        if d + w < dist[i]:
            dist[i] = d + w
            heappush(heap, (dist[i], i))

print(dist[-1])