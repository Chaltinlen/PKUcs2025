from collections import deque
ans = []
class treeNode:
    def __init__(self, name, deg):
        self.name = name
        self.deg = deg
        self.val = []

def backTra(tree):
    for node in tree.val:
        backTra(node)
    ans.append(tree.name)

tree_seq = [input().split() for i in range(int(input()))]
for seq in tree_seq:
    node = deque()
    queue = deque()
    queue.append(node)
    for i in range(0, len(seq), 2):
        node.append(treeNode(seq[i], int(seq[i + 1])))
    queue = deque()
    head = node[0]
    queue.append(node.popleft())
    while queue:
        n = queue.popleft()
        for i in range(n.deg):
            n.val.append(node.popleft())
            queue.append(n.val[-1])
    backTra(head)
print(*ans)