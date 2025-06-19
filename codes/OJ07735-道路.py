from heapq import heappush, heappop
from collections import defaultdict
K = int(input())
N = int(input())
R = int(input())
dist = defaultdict(list)
length = [[1e9 for j in range(K + 1)] for i in range(N + 1)]
length[1][0] = 0
for i in range(R):
    S, D, L, T = map(int, input().split())
    dist[S].append((L, T, D))
heap = [(0, 0, 1)]
ans = -1
while heap:
    distance, cost, node = heappop(heap)
    if node == N:
        ans = distance
        break
    if distance > length[node][cost]:
        continue
    for l, c, n in dist[node]:
        if c + cost <= K and l + distance < length[n][c + cost]:
            length[n][c + cost] = l + distance
            heappush(heap, (length[n][c + cost], c + cost, n))

print(ans)
