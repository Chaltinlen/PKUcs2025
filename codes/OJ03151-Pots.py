from math import gcd
ans = []
def exgcd(a, b):
    if b == 0:
        x = 1
        y = 0
        return x, y
    x1, y1 = exgcd(b, a % b)
    x = y1
    y = x1 - a // b * y1
    return x, y
def FILL(i):
    pot[i] = V[i]
    ans.append(f"FILL({i})")
def POUR(i):
    j = 3 - i
    print(i, j)
    print(pot[i], pot[j])
    pot[i], pot[j] = max(pot[i] + pot[j] - V[j], 0), min(pot[i] + pot[j], V[j])
    ans.append(f"POUR({i},{j})")
def DROP(i):
    pot[i] = 0
    ans.append(f"DROP({i})") 

A, B, C = map(int, input().split())
V = [0, A, B]
if C % gcd(A, B):
    print("impossible")
    exit()
coinf = tuple([0]) + exgcd(A, B)
print(coinf)
pot = [0, 0, 0]
for i in range(1, 3):
    if coinf[i] > 0:
        j = 3 - i
        print(j, pot)
        print(pot[j])
        for _ in range(coinf[i]):
            FILL(i)
            POUR(i)
            if pot[j] == V[j]:
                DROP(j)
                if pot[i]:
                    POUR(i)
print(len(ans))
print(*ans, sep="\n")