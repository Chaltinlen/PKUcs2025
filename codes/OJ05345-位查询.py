N, M = map(int, input().split())
integer = list(map(int, input().split()))
for i in range(M):
    prom = input().split()
    prom[1] = int(prom[1])
    if prom[0] == "C":
        for j in range(N):
            integer[j] = (integer[j] + prom[1]) % 65536
    else:
        cnt = 0
        for n in integer:
            cnt += (n >> prom[1]) & 1
        print(cnt)
