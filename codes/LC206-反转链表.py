# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        bfr = head
        node = bfr.next
        bfr.next = None
        while node.next != None:
            aft = node.next
            node.next = bfr
            bfr = node
            node = aft
        node.next = bfr
        return node