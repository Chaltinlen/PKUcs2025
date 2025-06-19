from math import ceil
n, m = map(int, input().split())
kids = list(map(lambda t: ceil(int(t) / m), input().split()))
print(n - kids[::-1].index(max(kids)))
