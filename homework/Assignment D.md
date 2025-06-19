# Assignment \#D: 图 & 散列表

Updated 2042 GMT+8 May 20, 2025

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

### M17975: 用二次探查法建立散列表

http://cs101.openjudge.cn/practice/17975/

<mark>需要用这样接收数据。因为输入数据可能分行了，不是题面描述的形式。OJ上面有的题目是给C++设计的，细节考虑不周全。</mark>

```python
import sys
input = sys.stdin.read
data = input().split()
index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1
num_list = [int(i) for i in data[index:index+n]]
```



思路：
- 被重复数据卡了，没想到有重复的


代码：

```python
from sys import stdin
readin = map(int, stdin.read().split())
N = next(readin)
M = next(readin)
hashtable = [0] * M
pos = [0] * N
nums = []
for i in range(N):
    nums.append(next(readin))
for i in range(N):
    j = 0
    h = nums[i] % M
    p = h
    while hashtable[p] and hashtable[p] != nums[i]:
        p = (h + (-1 if j % 2 else 1) * (j // 2 + 1)**2) % M
        j += 1
    pos[i] = p
    hashtable[p] = nums[i]
print(*pos)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![OJ-17975](https://raw.githubusercontent.com/Chaltinlen/PKUcs2025/master/pics/OJ-17975.png)




### M01258: Agri-Net

MST, http://cs101.openjudge.cn/practice/01258/

思路：
- 最小生成树
- 之前我想了好久最小生成树的权值是不是等于全源最短路中的最小一行的和，应该是不等于


代码：

```python
from sys import stdin
from heapq import heappush, heappop, heapify
readin = map(int, stdin.read().split())
while True:
    try:
        N = next(readin)
    except StopIteration:
        break
    adj_mat = []
    for i in range(N):
        adj_mat.append([])
        for j in range(N):
            adj_mat[-1].append(next(readin))
    heap = [(adj_mat[0][i], i) for i in range(1, N)]
    heapify(heap)
    vis = {0}
    ans = 0
    while True:
        d, i = heappop(heap)
        if i in vis:
            continue
        ans += d
        vis.add(i)
        if len(vis) == N:
            break
        for n in range(N): 
            if n not in vis:
                heappush(heap, (adj_mat[i][n], n))
    print(ans)

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![OJ-01258](https://raw.githubusercontent.com/Chaltinlen/PKUcs2025/master/pics/OJ-01258.png)



### M3552.网络传送门旅游

bfs, https://leetcode.cn/problems/grid-teleportation-traversal/

思路：
- 你要干啥
- 你卡你那常数你想干啥
- 改一晚上也改不出来，出题人你想干啥
- 抄的答案


代码：

```python
from typing import *
from collections import deque, defaultdict
class Solution:
    def minMoves(self, matrix: List[str]) -> int:
        if matrix[-1][-1] == '#':
            return -1
        inf = float("inf")
        m, n = len(matrix), len(matrix[0])
        pos = defaultdict(list)
        for i, row in enumerate(matrix):
            for j, c in enumerate(row):
                if c.isupper():
                    pos[c].append((i, j))

        DIRS = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        dis = [[inf] * n for _ in range(m)]
        dis[0][0] = 0
        q = deque([(0, 0)])

        while q:
            x, y = q.popleft()
            d = dis[x][y]

            if x == m - 1 and y == n - 1:  # 到达终点
                return d

            c = matrix[x][y]
            if c in pos:
                # 使用所有传送门
                for px, py in pos[c]:
                    if d < dis[px][py]:
                        dis[px][py] = d
                        q.appendleft((px, py))
                del pos[c]  # 避免重复使用传送门

            # 下面代码和普通 BFS 是一样的
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] != '#' and d + 1 < dis[nx][ny]:
                    dis[nx][ny] = d + 1
                    q.append((nx, ny))

        return -1



if __name__ == "__main__":
    sol = Solution()
    print(sol.minMoves([".P..#.S............D........",".....X......V..........TT...","Q.E...K.........L..Q...XD...","............................","............................","............................","............................","............................","............................","............................","............................","............................","............................","............................","............................","............................","............................","............................","............................","............................","............................","............................","............................","............................","............................","............................","............................","............................","............................","............................","............................","............................","............................","............................","............................","............................","............................","............................"]))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![LC-3552](https://raw.githubusercontent.com/Chaltinlen/PKUcs2025/master/pics/LC-3552.png)




### M787.K站中转内最便宜的航班

Bellman Ford, https://leetcode.cn/problems/cheapest-flights-within-k-stops/

思路：
- 和月考题很像


代码：

```python
from typing import *
from heapq import heappush, heappop
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_mat = [[1000001 for i in range(n)] for j in range(n)]
        for s, c, p in flights:
            adj_mat[s][c] = p
        dist = [[1000001 for i in range(k + 2)] for j in range(n)]
        heap = [(0, 0, src)]
        ans = -1
        while heap:
            c, ret, node = heappop(heap)
            if dist[node][ret] < c:
                continue
            if node == dst:
                ans = c
                break
            for i in range(n):
                if adj_mat[node][i] < 10001 and ret <= k and c + adj_mat[node][i] < dist[i][ret + 1]:
                    dist[i][ret + 1] = c + adj_mat[node][i]
                    heappush(heap, (dist[i][ret + 1], ret + 1, i))
        return ans



if __name__ == "__main__":
    sol = Solution()
    print(sol.findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1))

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![LC-787](https://raw.githubusercontent.com/Chaltinlen/PKUcs2025/master/pics/LC-787.png)




### M03424: Candies

Dijkstra, http://cs101.openjudge.cn/practice/03424/

思路：
- 先省略100字对作者的情感输出
- 我写的代码全部WA，AI写的代码（包括手上拿着答案的小北explore在内）全部TLE
代码：
- Dijkstra算法，WA
```python
from heapq import heappush, heappop

N, M = map(int, input().split())
adj_mat = [[float("inf")] * N for _ in range(N)]
for _ in range(M):
    a, b, c = map(int, input().split())
    adj_mat[a-1][b-1] = c

dist = [float("inf")] * N
dist[0] = 0
heap = [(0, 0)]
visited = [False] * N

while heap:
    d, node = heappop(heap)
    if node == N - 1:
        break
    if visited[node]:
        continue
    visited[node] = True
    for i in range(N):
        if adj_mat[node][i] != float("inf") and d + adj_mat[node][i] < dist[i]:
            dist[i] = d + adj_mat[node][i]
            heappush(heap, (dist[i], i))

print(dist[-1])
```
- Bellman-Ford算法，WA
```python
from collections import deque
N, M = map(int, input().split())
edge = [[1e5 for i in range(N)] for j in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    edge[a-1][b-1] = c
queue = deque()
vis = [False] * (N + 1)
queue.append(0)
while queue:
    node = queue.popleft()
    vis[node] = False
    for i in range(N):
        if edge[node][i] < 1e5 and edge[0][i] > edge[0][node] + edge[node][i]:
            edge[0][i] = edge[0][node] + edge[node][i]
            if not vis[i]:
                queue.append(i)
                vis[i] = True
print(edge[0][-1])
```
- Floyd-Warshall算法，WA
```python
N, M = map(int, input().split())
edge = [[1e11 for i in range(N)] for j in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    edge[a-1][b-1] = c
for k in range(N):
    for i in range(N):
        for j in range(N):
            edge[i][j] = min(edge[i][j], edge[i][k] + edge[k][j])

print(edge[0][-1])
```
- 好，就在我编辑这份即将上交的作业的时候，我又交了一次，ac了，我不过是把第一次提交的代码中邻接矩阵改成了邻接表
- 那我不禁要问了，是作者分糖的时候左脑攻击右脑尖尖开始思考了吗？刚说完右边的哥们只准比我多一个，过了三秒钟说，右边的哥们只准比我多两个，那我听哪个？用邻接矩阵就是，听你最新版的指令，用邻接表那就是我管你这的那的我听最小的
```python
from heapq import heappush, heappop
N, M = map(int, input().split())
adj_mat = [[] for j in range(N)]
heap = []
for i in range(M):
    a, b, c = map(int, input().split())
    adj_mat[a-1].append((b-1, c))
dist = [1e11 for i in range(N)]
heap = [(0, 0)]
while heap:
    d, node = heappop(heap)
    if node == N - 1:
        dist[-1] = d
        break
    for i, w in adj_mat[node]:
        if d + w < dist[i]:
            dist[i] = d + w
            heappush(heap, (dist[i], i))

print(dist[-1])
```
- 更难听的话还是不骂了
- 耽误我一下午
代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![OJ-03424](https://raw.githubusercontent.com/Chaltinlen/PKUcs2025/master/pics/OJ-03424.png)

- 第22次提交的是网上搜到的能通过的C++代码



### M22508:最小奖金方案

topological order, http://cs101.openjudge.cn/practice/22508/

思路：
- 拓扑排序，和月考题有一定的相似之处


代码：

```python
from collections import deque
n, m = map(int, input().split())
d = [[] for i in range(n)]
deg = [0 for i in range(n)]
prize = [0 for i in range(n)]
queue = set(range(n))
for i in range(m):
    a, b = map(int, input().split())
    d[b].append(a)
    deg[a] += 1
    queue -= {a}
queue = deque(queue)
while queue:
    node = queue.popleft()
    for i in d[node]:
        deg[i] -= 1
        if not deg[i]:
            prize[i] = prize[node] + 1
            queue.append(i)

print(100 * n + sum(prize))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>
![OJ-22508](https://raw.githubusercontent.com/Chaltinlen/PKUcs2025/master/pics/OJ-22508.png)




## 2. 学习总结和收获

<mark>如果发现作业题目相对简单，有否寻找额外的练习题目，如“数算2025spring每日选做”、LeetCode、Codeforces、洛谷等网站上的题目。</mark>

写完作业我很生气因为我是弱智111