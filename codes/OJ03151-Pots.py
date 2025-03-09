ans = []
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

print(len(ans))
print(*ans, sep="\n")