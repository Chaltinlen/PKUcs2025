n = int(input())
s = list(map(int, input().split()))
nums = list(range(n, 0, -1))
stack = [0]
for i in s:
    while i > stack[-1]:
        stack.append(nums.pop())
        print(stack, nums)
    if i == stack[-1]:
        stack.pop()
        print(i, stack, nums)
    else:
        print("No")
        exit()
print("Yes")
