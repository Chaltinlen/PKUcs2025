while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    res = 0
    for i in range(2, 1 + n):
        res = (res + m) % i
    print(res + 1)
