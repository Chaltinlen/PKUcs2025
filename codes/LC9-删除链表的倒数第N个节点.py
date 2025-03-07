# Definition for singly-linked list.
from typing import *
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        lastslow = head
        cnt = 0
        while fast.next:
            fast = fast.next
            if cnt == n - 1:
                slow = slow.next
            if cnt >= n:
                slow = slow.next
                lastslow = lastslow.next
            cnt += 1
        if slow == lastslow:
            return slow.next
        elif slow == fast:
            lastslow.next = None
            return head
        else:
            lastslow.next = slow.next
            return head
