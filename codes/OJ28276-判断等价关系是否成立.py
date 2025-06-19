table = {}
def find(a):
    return a if table[a] == a else find(table[a])
def merge(x, y):
    table[find(x)] = find(y)
n = int(input())
check = []
for i in range(n):
    e = input()
    x, s, y = e[0], e[1], e[-1]
    if x not in table:
        table[x] = x
    if y not in table:
        table[y] = y
    if s == '!':
        check.append((x, y))
    elif s == '=':
        merge(x, y)
ans = True
for x, y in check:
    ans &= (find(x) != find(y))
print(ans)