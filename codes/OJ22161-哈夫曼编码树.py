from heapq import heappop, heappush
code = {}
decode = {}
heap = []
class TreeNode:
    def __init__(self, ch, freq, minch="", left=None, right=None):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right
        self.minch = list(ch)[0] if not minch else minch
    def __lt__(self, other):
        return (self.freq, self.minch) < (other.freq, other.minch)
    def __add__(self, other):
        return TreeNode(
            self.ch | other.ch,
            self.freq + other.freq,
            min(self.minch, other.minch),
            self if self < other else other,
            other if self < other else self
            )

def encode(node, prev):
    if not node:
        return
    if not node.left and not node.right:
        c = list(node.ch)[0]
        code[c] = prev
        decode[prev] = c
        return
    encode(node.left, prev + "0")
    encode(node.right, prev + "1")

def num_to_str(get):
    ans = ""
    lst = 0
    for i in range(1, len(get) + 1):
        if get[lst:i] in decode:
            ans += decode[get[lst:i]]
            lst = i
    return ans

def str_to_num(get):
    ans = ""
    for c in get:
        ans += code[c]
    return ans

for i in range(int(input())):
    c, f = input().split()
    heappush(heap, TreeNode({c}, int(f)))
while len(heap) > 1:
    n1 = heappop(heap)
    n2 = heappop(heap)
    node = n1 + n2
    heappush(heap, node)
head = node
encode(head, "")
while True:
    try:
        get = input()
        if get[0] in {"0", "1"}:
            print(num_to_str(get))
        else:
            print(str_to_num(get))
    except EOFError:
        break