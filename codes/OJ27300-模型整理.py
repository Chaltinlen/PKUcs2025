from itertools import groupby
n = int(input())
model = [input().split("-") for i in range(n)]
trans = {"B": 1000, "M": 1}
for i in range(n):
    rate = float(model[i][-1][:-1]) * trans[model[i][-1][-1]]
    model[i].insert(1, rate)
    model[i] = tuple(model[i])
model.sort()

for key, val in groupby(model, key=lambda t: t[0]):
    rates = [t[-1] for t in val]
    print(f"{key}: ", end="")
    print(*rates, sep=", ")
