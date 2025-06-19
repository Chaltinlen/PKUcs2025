pst = []
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pstT(node):
    if node:
        pstT(node.left)
        pstT(node.right)
        pst.append(node.val)
# def build(lo, hi, i):
#     if lo < hi:
#         print(lo, hi, i)
#         val = pre[i]
#         node = TreeNode(val)
#         ind = mid.index(val)
#         node.left = build(lo, ind - 1, i + 1)
#         node.right = build(ind, hi, i + ind - lo)
#         return node
def construct(prefix, infix):
    if not prefix:
        return None
    head = TreeNode(prefix[0])
    p = infix.index(prefix[0])
    head.left = construct(prefix[1:p + 1], infix[:p])
    head.right = construct(prefix[p + 1:], infix[p + 1:])
    return head
n = int(input())
pre = list(map(int, input().split()))
mid = sorted(pre)
pstT(construct(pre, mid))
print(*pst)