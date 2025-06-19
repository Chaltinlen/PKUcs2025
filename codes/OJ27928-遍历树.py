class TreeNode:
    def __init__(self, val):
        self.val = val
        self.subnode = []

def get_height(node):
    if node in height:
        return
    if nodes[node].subnode == []:
        height[node] = 1
        return
    for n in nodes[node].subnode:
        if n.val not in height:
            get_height(n.val)
    height[node] = max([height[n.val] for n in nodes[node].subnode]) + 1

def print_tree(node):
    for n in sorted(nodes[node].subnode + [nodes[node]], key=lambda t: int(t.val)):
        if n == nodes[node]:
            ans.append(n.val)
        else:
            print_tree(n.val)

nodes = {}
for i in range(int(input())):
    vals = input().split()
    for v in vals:
        if v not in nodes:
            nodes[v] = TreeNode(v)
    if len(vals) > 1:
        for v in vals[1:]:
            nodes[vals[0]].subnode.append(nodes[v])
height = {}
for n in nodes:
    get_height(n)
ans = []
print_tree(max(height, key=lambda t: height[t]))
print(*ans, sep="\n")