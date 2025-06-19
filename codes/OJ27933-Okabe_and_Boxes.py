stack = []
n = int(input())
ans = 0
cnt = 0
prompt = [input().split() for i in range(2 * n)]
i = 0
while i < 2 * n:
    p = prompt[i]
    if p[0] == "add":
        stack.append(int(p[1]))
    else:
        cnt += 1
        if stack[-1] == cnt:
            stack.pop()
        else:
            ans += 1
            stack.sort(reverse=True)
            stack.pop()
    i += 1
print(ans)