parti = "|     "
cnt = 0
class TreeNode:
    def __init__(self, val, ctp=None):
        self.val = val
        self.dir = []
        self.file = []
        self.s = ""
        self.ctp = ctp

def show(node, layer):
    print(layer * parti + node.val)
    if node.dir:
        for d in node.dir:
            show(d, layer + 1)
    if node.file:
        for f in sorted(node.file):
            print(layer * parti + f)

while True:
    cnt += 1
    root = TreeNode("ROOT")
    p = root
    while((s := input()) not in "*#"):
        if s[0] == "f":
            p.file.append(s)
        elif s[0] == "d":
            p.dir.append(TreeNode(s))
            p.dir[-1].ctp = p
            p = p.dir[-1]
        elif s[0] == "]":
            p = p.ctp
    
    if s == "#":
        break
    print(f"DATA SET {cnt}:")
    show(root, 0)
    print()