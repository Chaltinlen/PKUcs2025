from sys import stdin
get = stdin.read().split()
for a in get:
    print(["NO", "YES"][a == "".join(reversed(a))])
