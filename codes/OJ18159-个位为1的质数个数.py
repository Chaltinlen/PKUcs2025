from bisect import bisect_left
prime = []
isprime = [True] * 10001
isprime[0] = isprime[1] = False
for i in range(2, 10001):
    if isprime[i]:
        prime.append(i)
    for j in prime:
        if i * j >= 10001:
            break
        isprime[i * j] = False
        if i % j == 0 and j != i:
            break
prime1 = [p for p in prime if p % 10 == 1]
for i in range(1, 1 + int(input())):
    ans = []
    n = int(input())
    print(f"Case{i}:")
    if n <= 11:
        print("NULL")
    else:
        ind = bisect_left(prime1, n)
        ans = prime1[:ind]
        print(*ans)
