from collections import defaultdict
from heapq import heappush, heappop, heapify
n = int(input())
adj_tab = defaultdict(list)
for i in range(n-1):
    s = input().split()
    c = s[0]
    m = int(s[1])
    for j in range(2, len(s), 2):
        adj_tab[c].append((int(s[j + 1]), s[j]))
        adj_tab[s[j]].append((int(s[j + 1]), c))
vis = set()
heap = [(0, 'A')]
ans = 0
while heap:
    d, node = heappop(heap)
    if node in vis:
        continue
    vis.add(node)
    ans += d
    if len(vis) == n:
        break
    for r, star in adj_tab[node]:
        if star not in vis:
            heappush(heap, (r, star))

print(ans)

