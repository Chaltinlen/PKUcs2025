from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        s = ""
        h = self
        while h:
            s += str(h.val) + "->"
            h = h.next
        return s[:-2]
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(L1, L2):
            if not L1:
                return L2
            if not L2:
                return L1
            h1, h2 = L1, L2
            head = ListNode()
            p = head
            while h1 and h2:
                h1n = h1.next
                h2n = h2.next
                if h1.val > h2.val:
                    p.next = h2
                    p = p.next
                    h2 = h2n
                else:
                    p.next = h1
                    p = p.next
                    h1 = h1n
            if h1:
                p.next = h1
            else:
                p.next = h2
            return head.next


        if not lists:
            return None
        ans = lists[0]
        for i in range(1, len(lists)):
            ans = merge(ans, lists[i])
        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.mergeKLists([ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))]))