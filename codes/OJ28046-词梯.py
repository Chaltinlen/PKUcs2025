from collections import deque, defaultdict
def find_barrel(word):
    for c in range(len(word)):
        yield word[:c] + " " + word[c+1:]
words = [input() for i in range(int(input()))]
barrels = defaultdict(list)
for word in words:
    for b in find_barrel(word):
        barrels[b].append(word)
start, end = input().split()
queue = deque([(start, [])])
inq = {start}
while queue:
    node, route = queue.popleft()
    if node == end:
        print(*(route + [node]))
        exit()
    for b in find_barrel(node):
        for w in barrels[b]:
            if w not in inq and b != node:
                inq.add(w)
                queue.append((w, route + [node]))

print("NO")