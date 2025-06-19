# Definition for singly-linked list.
from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        p, q = head, head
        if not p:
            return head
        while q.next and q.next.next:
            p = p.next
            q = q.next.next
        q = p.next
        p.next = None
        p = head
        bfr = q
        if q and q.next:
            q = q.next
            bfr.next = None
            while q.next:
                aft = q.next
                q.next = bfr
                bfr = q
                q = aft
            q.next = bfr
        while q:
            if p.val == q.val:
                p = p.next
                q = q.next
            else:
                return False
        return True

if __name__ == '__main__':
    sol = Solution()
    head = ListNode(8)
    p = head
    for n in [0,7,1,7,7,9,7,5,2,9,1,7,3,7,0,6,5,1,7,7,9,3,8,1,5,7,7,8,4,0,9,3,7,3,4,5,7,4,8,8,5,8,9,8,5,8,8,4,7,5,4,3,7,3,9,0,4,8,7,7,5,1,8,3,9,7,7,1,5,6,0,7,3,7,1,9,2,5,7,9,7,7,1,7,0,8]:
        p.next = ListNode(n)
        p = p.next
    print(sol.isPalindrome(head))
