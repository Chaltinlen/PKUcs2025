pre, mid, pst = [], [], []
class TreeNode:
    def __init__(self, val, left=None, right=None, ctp=None):
        self.val = val
        self.left = left
        self.right = right
        self.ctp = ctp
def preT(root):
    if root != None and root.val != "*":
        pre.append(root.val)
        preT(root.left)
        mid.append(root.val)
        preT(root.right)
        pst.append(root.val)

for i in range(int(input())):
    pre, mid, pst = [], [], []
    root = TreeNode(input())
    slash = 0
    p = root
    while ((s := input()) != "0"):
        ns = s.count("-")
        node = TreeNode(s[-1])
        if ns > slash:
            p.left = node
            node.ctp = p
            p = p.left
        else:
            for i in range(slash - ns + 1):
                p = p.ctp
            p.right = node
            node.ctp = p
            p = p.right
        slash = ns

    preT(root)
    print("".join(pre), "".join(pst), "".join(mid), sep="\n")
    print()