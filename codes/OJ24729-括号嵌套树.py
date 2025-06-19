bracket = input()
print("".join(filter(str.isalpha, bracket)))
stack = []
ans = []
temp = []
for c in bracket:
    if c != ')':
        if c != ',':
            stack.append(c)
        else:
            ans.append(stack.pop())

    else:
        temp = []
        while((s := stack.pop()) != '('):
            ans.append(s)
ans.append(stack.pop())
print("".join(ans))