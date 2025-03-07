from copy import copy
N = int(input())
table = [set() for i in range(N)]
file = set()
for i in range(N):
    table[i] = set(map(int, input().split()[1:]))
    file |= table[i]
M = int(input())
for i in range(M):
    ans = copy(file)
    quest = input().split()
    for j in range(N):
        if quest[j] == "1":
            ans &= table[j]
        elif quest[j] == "-1":
            ans -= table[j]
    if ans:
        print(" ".join(map(str, sorted(ans))))
    else:
        print("NOT FOUND")
