from collections import deque
n, m = map(int, input().split())
d = [[] for i in range(n)]
deg = [0 for i in range(n)]
prize = [0 for i in range(n)]
queue = set(range(n))
for i in range(m):
    a, b = map(int, input().split())
    d[b].append(a)
    deg[a] += 1
    queue -= {a}
queue = deque(queue)
while queue:
    node = queue.popleft()
    for i in d[node]:
        deg[i] -= 1
        if not deg[i]:
            prize[i] = prize[node] + 1
            queue.append(i)

print(100 * n + sum(prize))