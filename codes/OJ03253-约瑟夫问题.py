# class CycleChainedList:
#     def __init__(self, val = 0, next = None):
#         self.val = val
#         self.next = next


# def exile(n, p, m):
#     if m == 0:
#         exit()
#     head = CycleChainedList(p)
#     q = head
#     for i in range(p + 1, p + n):
#         q.next = CycleChainedList((i - 1) % n + 1)
#         q = q.next
#     q.next = head
#     bfr = q
#     q = q.next
#     for i in range(n):
#         for j in range(m - 1):
#             q = q.next
#             bfr = bfr.next
#         yield q.val
#         bfr.next = q.next
#         q = q.next


from collections import deque
def exile(n, p, m):
    if m == 0:
        exit()
    queue = deque([(i - 1) % n + 1 for i in range(p, p + n)])
    for i in range(n):
        for j in range(m - 1):
            queue.append(queue.popleft())
        yield queue.popleft()


while True:
    print(*exile(*map(int, input().split())), sep=",")
