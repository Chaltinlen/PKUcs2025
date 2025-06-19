stack = []
for c in input():
    if c != "]":
        stack.append(c)
    else:
        temp = []
        t = 0
        while((n := stack.pop()) != "["):
            temp.append(n)
        for i in range(len(temp)-1, len(temp)-5, -1):
            if not temp[i].isdigit():
                t = int("".join(reversed(temp[i+1:])))
                temp = list(reversed(temp[:i+1]))
                break
        for i in range(t):
            stack += temp
print("".join(stack))

