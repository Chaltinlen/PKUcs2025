from sys import stdin
from heapq import heappush, heappop, heapify
readin = map(int, stdin.read().split())
while True:
    try:
        N = next(readin)
    except StopIteration:
        break
    adj_mat = []
    for i in range(N):
        adj_mat.append([])
        for j in range(N):
            adj_mat[-1].append(next(readin))
    heap = [(adj_mat[0][i], i) for i in range(1, N)]
    heapify(heap)
    vis = {0}
    ans = 0
    while True:
        d, i = heappop(heap)
        if i in vis:
            continue
        ans += d
        vis.add(i)
        if len(vis) == N:
            break
        for n in range(N):
            if n not in vis:
                heappush(heap, (adj_mat[i][n], n))
    print(ans)
