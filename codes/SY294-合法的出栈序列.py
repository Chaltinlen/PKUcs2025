n = int(input())
s = list(map(int, input().split()))
nums = list(range(n, 0, -1))
stack = [0]
for i in s:
    while i > stack[-1]:
        stack.append(nums.pop())
    if i == stack[-1]:
        stack.pop()
    else:
        print("No")
        exit()
print("Yes")
