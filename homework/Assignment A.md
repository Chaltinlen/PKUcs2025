# Assignment \#A: Graph starts

Updated 1830 GMT+8 Apr 22, 2025

2025 spring, Complied by <mark>颜鼎堃 工学院</mark>



> **说明：**
>
> 1. **解题与记录：**
>
>    对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
> 2. **提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
>
> 3. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。 
>
> 请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。



## 1. 题目

### M19943:图的拉普拉斯矩阵

OOP, implementation, http://cs101.openjudge.cn/practice/19943/

要求创建Graph, Vertex两个类，建图实现。

思路：
- 想起来线性代数课上老师讲过这个


代码：

```python
class Vertex:
    def __init__(self, n, D=[[]]):
        self.D = D
        for i in range(n):
            for j in range(n):
                D[-1].append(0)
            D.append([])
class Graph:
    def __init__(self, n, A=[[]]):
        self.A = A
        for i in range(n):
            for j in range(n):
                A[-1].append(0)
            A.append([])

n, m = map(int, input().split())
v = [Vertex(n)] * n
G = Graph(n)
ans = [[0 for j in range(n)] for i in range(n)]
for i in range(m):
    v1, v2 = map(int, input().split())
    v[v1].D[v1][v1] += 1
    v[v2].D[v2][v2] += 1
    G.A[v1][v2] = G.A[v2][v1] = 1
for i in range(n):
    for j in range(n):
        ans[i][j] = v[0].D[i][j] - G.A[i][j]
    print(*ans[i])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![[OJ-19943.png]]




### LC78.子集

backtracking, https://leetcode.cn/problems/subsets/

思路：
- 其实我一直没理解回溯是什么意思，反正大概应该就是递归吧


代码：

```python
from typing import *
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def recur(nums, depth, pref):
            if depth == len(nums):
                self.ans.append(pref)
                return
            recur(nums, depth + 1, pref)
            recur(nums, depth + 1, pref + [nums[depth]])

        recur(nums, 0, [])
        return self.ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.subsets([1, 2, 3]))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![[LC-78.png]]




### LC17.电话号码的字母组合

hash table, backtracking, https://leetcode.cn/problems/letter-combinations-of-a-phone-number/

思路：
- 跟子集差不多


代码：

```python
from typing import *
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        NUM_TO_LETTER = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        self.ans = []
        def recur(digits, depth, prev):
            if depth >= len(digits):
                self.ans.append(prev)
                return
            for n in NUM_TO_LETTER[digits[depth]]:
                recur(digits, depth + 1, prev + n)
        recur(digits, 0, "")
        if not self.ans[0]:
            self.ans.pop()
        return self.ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.letterCombinations(""))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![[LC-17.png]]




### M04089:电话号码

trie, http://cs101.openjudge.cn/practice/04089/

思路：
- 理解了前缀树会发现没那么难
- 最开始写的时候没考虑到可能会有相同的电话号码，我还专门把相同的电话号码设成了不矛盾
- 也就是下面第14行写的是`if p and "end" not in p:`
- 确实不太合理，不同的人怎么会用同一个电话号码呢
- 最后问了小北explore，回答是挺胡扯八道的，但代码是对的
- ai还是厉害，ai快取代我吧


代码：

```python hl=14
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
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![[OJ-04089.png]]




### T28046:词梯

bfs, http://cs101.openjudge.cn/practice/28046/

思路：
- 上课听到了做桶的思路，所以整体做起来没那么难


代码：

```python
from collections import deque, defaultdict
def find_barrel(word):
    for c in range(len(word)):
        yield word[:c] + " " + word[c+1:]
words = [input() for i in range(int(input()))]
barrels = defaultdict(list)
for word in words:
    for b in find_barrel(word):
        barrels[b].append(word)
start, end = input().split()
queue = deque([(start, [])])
inq = {start}
while queue:
    node, route = queue.popleft()
    if node == end:
        print(*(route + [node]))
        exit()
    for b in find_barrel(node):
        for w in barrels[b]:
            if w not in inq and b != node:
                inq.add(w)
                queue.append((w, route + [node]))

print("NO")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![[OJ-28046.png]]




### T51.N皇后

backtracking, https://leetcode.cn/problems/n-queens/

思路：
- 跟上学期八皇后一个思路


代码：

```python
from typing import *
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.ans = []
        def solve(n, depth, prev):
            if depth == n:
                self.ans.append(prev)
            for i in range(n):
                if i in prev:
                    continue
                for j in range(len(prev)):
                    if depth - i == j - prev[j] or depth + i == j + prev[j]:
                        break
                else:
                    solve(n, depth + 1, prev + [i])

        solve(n, 0, [])
        board = []
        for a in self.ans:
            board.append(["".join(["." if i != a[j] else "Q" for i in range(n)]) for j in range(n)])
        return board


if __name__ == "__main__":
    sol = Solution()
    print(sol.solveNQueens(4))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![[LC-51.png]]




## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>
这次作业因为上课听了点思路，做起来不是很难。如果上课没听到剧透，自己确实很难做出来了