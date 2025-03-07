from itertools import permutations
def is_possible(seq):
    n = len(seq)
    nums = list(range(n, 0, -1))
    stack = [0]
    for i in seq:
        while i > stack[-1]:
            stack.append(nums.pop())
        if i == stack[-1]:
            stack.pop()
        else:
            return False
    return True

    
for p in permutations(range(1, 1 + int(input()))):
    if is_possible(p):
        print(*p)
