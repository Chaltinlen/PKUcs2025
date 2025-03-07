from collections import defaultdict
table = defaultdict(list)
for i in range(1, int(input()) + 1):
    for w in input().split()[1:]:
        if not table[w] or (table[w] and table[w][-1] != i):
            table[w].append(i)
for i in range(int(input())):
    w = input()
    if table[w]:
        print(" ".join(map(str, table[w])))
    else:
        print("NOT FOUND")
