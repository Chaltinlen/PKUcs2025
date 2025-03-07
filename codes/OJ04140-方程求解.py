from math import pow
def f(x):
    return pow(x, 3) - 5 * pow(x, 2) + 10 * x - 80
def f_p(x):
    return 3 * pow(x, 2) - 10 * x + 10

# x_0 \in (5, 6)
# f''(x) = 6x - 10, f''(6) * f(6) > 0

x = 6
while f(x) * f(x - 5 * 1e-10) > 0:
    x = x - f(x) / f_p(x)
print(f"{x:.9f}")
