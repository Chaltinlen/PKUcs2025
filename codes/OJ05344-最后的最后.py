class circleLinkedList:
    def __init__(self, val, next):
        self.val = val
        self.next = next

n, k = map(int, input().split())
head = circleLinkedList(1, None)
p = head
for i in range(2, n + 1):
    p.next = circleLinkedList(i, None)
    p = p.next
p.next = head
for i in range(n - 1):
    for j in range(k - 1):
        head = head.next
        p = p.next
    p.next = head.next
    print(head.val, end=" ")
    head = head.next