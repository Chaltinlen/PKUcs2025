size = 0
def find(x):
    if belief[x] == x:
        return x
    return (x := find(belief[x]))
def join(x1, x2):
    global size
    f1 = find(x1)
    f2 = find(x2)
    if f1 != f2:
        size -= 1
        belief[f1] = f2
for _ in range(1, int(1e9)):
    n, m = map(int, input().split())
    if n == 0:
        break
    belief = [i for i in range(n + 1)]
    size = n
    for i in range(m):
        p, q = map(int, input().split())
        join(p, q)
    print(f"Case {_}: {size}")
