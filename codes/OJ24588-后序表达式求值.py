from collections import deque
for i in range(int(input())):
    exp = deque(input().split())
    oprand = []
    for token in exp:
        try:
            oprand.append(float(token))
        except ValueError:
            a = str(oprand.pop())
            b = str(oprand.pop())
            oprand.append(eval(b + token + a))
    print(f"{oprand[0]:.2f}")
