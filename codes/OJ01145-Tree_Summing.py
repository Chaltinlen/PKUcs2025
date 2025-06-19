from sys import stdin
class TreeNode:
    def  __init__(self, val, left=None, right=None, ctp=None):
        self.val = val
        self.left = left
        self.right = right
        self.ctp = ctp
def preT(s, node):
    s += node.val
    if node.left:
        preT(s, node.left)
    if node.right:
        preT(s, node.right)
    if not (node.left or node.right):
        global I
        ans[-1] |= (s == I)
readin = stdin.read()
trees = []
nums = [[]]
cnt = 0
for c in readin:
    if c == ' ' or c == '\n':
        continue
    if c == '(':
        cnt += 1
        if cnt == 1:
            trees.append([])
    if cnt:
        trees[-1].append(c)
    else:
        nums[-1].append(c)
    if c == ')':
        cnt -= 1
        if cnt == 0:
            nums.append([])
nums.pop()
ans = []
for i in range(len(nums)):
    I = int("".join(nums[i]))
    T = trees[i]
    ans.append(False)
    root = TreeNode(0)
    p = root
    num_stack = []
    for ind in range(len(T)):
        if T[ind].isdigit():
            num_stack.append(T[ind])
            if not (T[ind + 1].isdigit() or T[ind + 1] == '-'):
                break
    if num_stack:
        root.val = int("".join(num_stack))
    num_stack = []
    j = ind + 1
    while j < len(T) - 1:
        c = T[j]
        if c == '(':
            if T[j + 1] == ')':
                j += 2
                continue
            p.left = TreeNode(0, ctp=p)
            p = p.left
            j += 1
            continue
        elif c == ')':
            if T[j + 1] == ')':
                j += 1
                p = p.ctp
                continue
            elif T[j + 1] == '(':
                p = p.ctp
                if T[j + 2] == ')':
                    j += 3
                    continue
                p.right = TreeNode(0, ctp=p)
                p = p.right
                j += 2
                continue
        elif c.isdigit() or c == '-':
            num_stack.append(c)
            if T[j + 1].isdigit() or T[j + 1] == '-':
                j += 1
                continue
            else:
                p.val = int("".join(num_stack))
                num_stack = []
                j += 1
                continue
    preT(0, root)
for b in ans:
    if b:
        print("yes")
    else:
        print("no")
