# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # searched = set()
        # p = headA
        # while p:
        #     searched.add(p)
        #     p = p.next
        # p = headB
        # while p:
        #     if p in searched:
        #         return p
        #     p = p.next
        # return None

        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A
