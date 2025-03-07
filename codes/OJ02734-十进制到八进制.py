a = int(input())
stack = []
while (div := a // 8):
    stack.append(a % 8)
    a = div
stack.append(a)
while stack:
    print(stack.pop(), end="")
