class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                temp = []
                num = ""
                t = 0
                while((n := stack.pop()) != "["):
                    temp.append(n)
                try:
                    while((n := stack.pop()).isdigit()):
                        num = n + num
                    stack.append(n)
                except IndexError:
                    pass
                t = int(num)
                stack += list(reversed(temp)) * t
        return "".join(stack)

if __name__ == '__main__':
    sol = Solution()
    print(sol.decodeString("2[ab20[cd]]3[cd]ef"))