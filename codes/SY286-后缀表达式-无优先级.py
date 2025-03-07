exp = input().split()
opstack = []
ans = []
for token in exp:
    if token.isdigit():
        ans.append(token)
    else:
        while opstack:
            ans.append(opstack.pop())
        opstack.append(token)
while opstack:
    ans.append(opstack.pop())
print(" ".join(ans))
