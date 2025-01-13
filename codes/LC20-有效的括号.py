class Solution:
    def isValid(self, s: str) -> bool:
        brk = []
        left_brak = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in left_brak.values():
                brk.append(c)
            else:
                if brk and brk[-1] == left_brak[c]:
                    brk.pop()
                else:
                    return False
        if brk:
            return False
        else:
            return True
if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid(input()))
