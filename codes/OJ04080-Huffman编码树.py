from heapq import heappush, heappop
ans = 0
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __lt__(self, other):
        return self.val < other.val

def calcWeighedLength(node, h):
    if node and not node.left and not node.right:
        global ans
        ans += h * node.val
        return
    calcWeighedLength(node.left, h + 1)
    calcWeighedLength(node.right, h + 1)
heap = []
n = int(input())
weight = map(int, input().split())
for i in weight:
    heappush(heap, TreeNode(i))
while len(heap) >= 2:
    node1 = heappop(heap)
    node2 = heappop(heap)
    node = TreeNode(node1.val + node2.val, node1, node2)
    heappush(heap, node)
calcWeighedLength(node, 0)
print(ans)
