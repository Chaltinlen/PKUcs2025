from sys import stdin
ans = []
class TreeNode:
    def __init__(self, val="", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def construct(prefix, infix):
    if not prefix:
        return None
    head = TreeNode(prefix[0])
    p = infix.index(prefix[0])
    head.left = construct(prefix[1:p + 1], infix[:p])
    head.right = construct(prefix[p + 1:], infix[p + 1:])
    return head
def postTra(root):
    if root:
        postTra(root.left)
        postTra(root.right)
        ans.append(root.val)
seqs = stdin.read().split()
for i in range(0, len(seqs), 2):
    ans = []
    postTra(construct(seqs[i], seqs[i + 1]))
    print(*ans, sep="")