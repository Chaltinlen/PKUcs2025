from collections import deque
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        queue = deque()
        M = -1
        arr.append(-1)
        for i in range(len(arr) - 1):
            M = max(arr.pop(), M)
            queue.appendleft(M)
        return list(queue)