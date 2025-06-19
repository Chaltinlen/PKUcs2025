class TreeNode:
    def __init__(self, val="*", left=None, right=None, ctp=None):
        self.val = val
        self.left = left
        self.right = right
        self.ctp = ctp
def T(node):
    if node and node.val != "*":
        pre.append(node.val)
        T(node.left)
        mid.append(node.val)
        T(node.right)
for i in range(int(input())):
    pre, mid = [], []
    s = input()
    root = TreeNode(s[0])
    p = root
    for c in s[1:]:
        if c == "(":
            n = TreeNode(ctp=p)
            p.left = n
            p = p.left
        elif c == ",":
            p = p.ctp
            n = TreeNode(ctp=p)
            p.right = n
            p = p.right
        elif c == ")":
            p = p.ctp
        else:
            p.val = c
    T(root)
    print("".join(pre) + "\n" + "".join(mid))

