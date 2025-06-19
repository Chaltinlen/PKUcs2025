from collections import deque
from sys import stdin
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert(n, p):
    if n < p.val:
        if p.left:
            insert(n, p.left)
        else:
            p.left = TreeNode(n)
    elif n > p.val:
        if p.right:
            insert(n, p.right)
        else:
            p.right = TreeNode(n)

data = list(map(int, stdin.read().split()))
head = TreeNode(data[0])
for num in data[1:]:
    insert(num, head)
queue = deque([head])
ans = []
while queue:
    node = queue.popleft()
    if not node:
        continue
    ans.append(str(node.val))
    queue.append(node.left)
    queue.append(node.right)
print(*ans, sep=" ", end="")