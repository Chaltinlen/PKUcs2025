# Assignment #3: 惊蛰 Mock Exam

Updated 1641 GMT+8 Mar 5, 2025

2025 spring, Complied by <mark>同学的姓名、院系</mark>



> **说明：**
>
> 1. **惊蛰⽉考**：AC4<mark>（请改为同学的通过数）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。
>
> 2. **解题与记录：**
>
>    对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
> 3. **提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
>
> 4. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。 
>
> 请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。



## 1. 题目

### E04015: 邮箱验证

strings, http://cs101.openjudge.cn/practice/04015



思路：
- 做过
- 考场上想用正则做但是失败了，看来还是正则功夫不到家


代码：

```python
from sys import stdin
mails = stdin.read().split()
for mail in mails:
    if mail[0] != "." and mail[0] != "@" and "@" in mail and ".@" not in mail and "@." not in mail and mail[-1] != "@" and mail[-1] != ".":
        left = mail[mail.index("@") + 1:]
        if "@" not in left and "." in left:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![OJ-04015](https://raw.githubusercontent.com/Chaltinlen/PKUcs2025/master/pics/OJ-04015.png)




### M02039: 反反复复

implementation, http://cs101.openjudge.cn/practice/02039/



思路：
- 有点像螺旋矩阵


代码：

```python
from pprint import pprint
DIRECTIONS = ((1, 0), (0, 1))
c = int(input())
coded = input()
n = len(coded)
a = 0
b = -1
matrix = [["0" for i in range(n // c)] for j in range(c)]
step = -1
for i in range(n):
    if i % c:
        a += step
    else:
        b += 1
        step = -step
    matrix[a][b] = coded[i]
for line in matrix:
    print("".join(line), end="")
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![OJ-02039](https://raw.githubusercontent.com/Chaltinlen/PKUcs2025/master/pics/OJ-02039.png)




### M02092: Grandpa is Famous

implementation, http://cs101.openjudge.cn/practice/02092/



思路：
- 看了好几遍题目才明白意思
- 其实不难
- ~~爷爷得了MVP，我就是town in go~~

代码：

```python
while True:
    N, M = map(int, input().split())
    if N == 0:
        break
    rankings = [list(map(int, input().split())) for i in range(N)]
    player = [-1] + [0] * 10000
    second = []
    for rank in rankings:
        for i in rank:
            player[i] += 1
    mvp = max(player)
    player[player.index(mvp)] = -1
    mvp = max(player)
    print(*[p for p in range(10001) if player[p] == mvp])
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![OJ-02092](https://raw.githubusercontent.com/Chaltinlen/PKUcs2025/master/pics/OJ-02092.png)



### M04133: 垃圾炸弹

matrices, http://cs101.openjudge.cn/practice/04133/



思路：
- 做过，有印象


代码：

```python
d = int(input())
n = int(input())
road = [[0 for i in range(1025)] for j in range(1025)]
for i in range(n):
    x, y, i = map(int, input().split())
    for row in range(max(0, x - d), min(1025, x + d + 1)):
        for col in range(max(0, y - d), min(1025, y + d + 1)):
            road[row][col] += i
max_gar = max(map(max, road))
cnt = 0
for i in road:
    cnt += i.count(max_gar)
print(cnt, max_gar)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![OJ-04133](https://raw.githubusercontent.com/Chaltinlen/PKUcs2025/master/pics/OJ-04133.png)




### T02488: A Knight's Journey

backtracking, http://cs101.openjudge.cn/practice/02488/



思路：
- 考场上看到这题，想到了另外一题，担心自己会超时，根本就没动笔
- 其实不难，后悔后悔
- 最大的收获是学会了怎样跳出递归


代码：

```python hl=5-6,19,33-36
from collections import deque
from math import ceil
DIRECTIONS = ((-1, -2), (1, -2), (-2, -1), (2, -1), (-2, 1), (2, 1), (-1, 2), (1, 2))
ans = "impossible"
class Found(Exception):
    pass


def check(coors):
    global ans
    ans = ""
    for i, j in coors:
        ans += chr(65 + j) + str(i + 1)
def dfs(x, y, path):
    # print(x, y, path)
    global p, q
    if len(path) == p * q:
        check(path)
        raise Found
    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < p and 0 <= ny < q and not board[nx][ny]:
            board[nx][ny] = 1
            dfs(nx, ny, path + [(nx, ny)])
            board[nx][ny] = 0


for i in range(1, 1 + int(input())):
    ans = "impossible"
    p, q = map(int, input().split())
    board = [[0 for i in range(q)] for j in range(p)]
    board[0][0] = 1
    try:
        dfs(0, 0, [(0, 0)])
    except Found:
        pass
    print(f"Scenario #{i}:\n" + ans + "\n")

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![OJ-02488](https://raw.githubusercontent.com/Chaltinlen/PKUcs2025/master/pics/OJ-02488.png)


### T06648: Sequence

heap, http://cs101.openjudge.cn/practice/06648/



思路：
- 不会写
- 让AI写了个，对着学习学习吧
- AI比我强太多

代码：

```python
import heapq

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        m = int(input[ptr])
        n = int(input[ptr+1])
        ptr += 2
        sequences = []
        for _ in range(m):
            seq = list(map(int, input[ptr:ptr+n]))
            ptr += n
            seq.sort()
            sequences.append(seq)
        if m == 0:
            continue  # as per problem constraints, m >0
        prev_sums = sequences[0].copy()
        for i in range(1, m):
            curr = sequences[i]
            heap = []
            for i_prev in range(n):
                s = prev_sums[i_prev] + curr[0]
                heapq.heappush(heap, (s, i_prev, 0))
            new_sums = []
            while len(new_sums) < n and heap:
                s, i_prev, j_curr = heapq.heappop(heap)
                new_sums.append(s)
                if j_curr + 1 < n:
                    next_j = j_curr + 1
                    next_s = prev_sums[i_prev] + curr[next_j]
                    heapq.heappush(heap, (next_s, i_prev, next_j))
            prev_sums = new_sums
        print(' '.join(map(str, prev_sums)))

if __name__ == "__main__":
    main()
```



代码运行截图 <mark>（AC代码截图，至少包含有"Accepted"）</mark>
![OJ-06648](https://raw.githubusercontent.com/Chaltinlen/PKUcs2025/master/pics/OJ-06648.png)




## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>
本来可以AC5的，倒数第二题让我想起了之前提到的一个题，据说很容易超时，就没尝试，最后一题又不会写
怎么感觉这学期这么不想学习呢，但自己又菜，那不完蛋了吗