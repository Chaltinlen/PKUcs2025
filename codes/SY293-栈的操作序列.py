n = int(input())
stack = []
for i in range(n):
    p = input().split()
    if p[0] == "push":
        stack.append(p[1])
    else:
        if stack:
            print(stack.pop())
        else:
            print("-1")