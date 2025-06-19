class Trie:
    def __init__(self):
        self.trie = {}
    def add(self, num):
        p = self.trie
        for n in num:
            if "end" in p:
                return False
            if n in p:
                p = p[n]
            else:
                p[n] = {}
                p = p[n]
        if p:
            return False
        p["end"] = True
        return True

for i in range(int(input())):
    t = Trie()
    flag = True
    for i in range(int(input())):
        flag &= t.add(input())
    print("YES" if flag else "NO")