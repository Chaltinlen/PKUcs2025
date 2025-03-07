# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from copy import deepcopy
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        bfr = deepcopy(head)
        node = bfr.next
        if not node:
            return True
        bfr.next = None
        while node.next != None:
            aft = node.next
            node.next = bfr
            bfr = node
            node = aft
        node.next = bfr
        while node:
            if node.val == head.val:
                node = node.next
                head = head.next
            else:
                return False
        return True