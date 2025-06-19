import sys
import heapq
from collections import deque, defaultdict

input = sys.stdin.readline

class DualHeap:
    def __init__(self):
        # 大根堆（存放较小的一半，用负数模拟）
        self.small = []  
        # 小根堆（存放较大的一半）
        self.large = []  
        # 延迟删除的记录
        self.delayed = defaultdict(int)
        # 两个堆中有效数据的个数
        self.small_size = 0  
        self.large_size = 0  

    def prune(self, heap):
        # 清理堆顶已经被延迟删除的元素，不再调整size（因为在remove中已扣减）
        if heap is self.small:
            while heap and self.delayed[-heap[0]] > 0:
                num = -heapq.heappop(heap)
                self.delayed[num] -= 1
        else:
            while heap and self.delayed[heap[0]] > 0:
                num = heapq.heappop(heap)
                self.delayed[num] -= 1

    def balance(self):
        # 保持 small 比 large 多 0 或 1 个有效元素
        if self.small_size > self.large_size + 1:
            self.prune(self.small)
            num = -heapq.heappop(self.small)
            self.small_size -= 1
            heapq.heappush(self.large, num)
            self.large_size += 1
        elif self.small_size < self.large_size:
            self.prune(self.large)
            num = heapq.heappop(self.large)
            self.large_size -= 1
            heapq.heappush(self.small, -num)
            self.small_size += 1

    def add(self, num):
        # 插入新数时，根据大小决定进入哪个堆
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
            self.small_size += 1
        else:
            heapq.heappush(self.large, num)
            self.large_size += 1
        self.balance()

    def remove(self, num):
        # 延迟删除：标记待删除，同时减少对应堆的有效元素数量
        self.delayed[num] += 1
        if self.small and num <= -self.small[0]:
            self.small_size -= 1
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.large_size -= 1
            if self.large and num == self.large[0]:
                self.prune(self.large)
        self.balance()

    def median(self):
        # 查询中位数前先清理堆顶
        self.prune(self.small)
        self.prune(self.large)
        total = self.small_size + self.large_size
        if total % 2 == 1:
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2

if __name__ == '__main__':
    n = int(input())
    dh = DualHeap()
    # 使用 deque 记录入队顺序，确保del操作删除最先添加的数
    q = deque()
    results = []
    for _ in range(n):
        parts = input().split()
        op = parts[0]
        if op == 'add':
            x = int(parts[1])
            dh.add(x)
            q.append(x)
        elif op == 'del':
            x = q.popleft()
            dh.remove(x)
        elif op == 'query':
            med = dh.median()
            # 若中位数为整数则去除小数部分
            if med == int(med):
                results.append(str(int(med)))
            else:
                results.append(str(med))
    print("\n".join(results))