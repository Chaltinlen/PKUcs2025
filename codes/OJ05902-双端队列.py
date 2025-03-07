class LinkedList:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
        self.size = 0
    def popleft(self):
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return
        self.head = self.head.next
        self.head.last = None
        self.size -= 1
    def pop(self):
        if self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return
        self.tail = self.tail.last
        self.tail.next = None
        self.size -= 1
    def append(self, node):
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
    def __str__(self):
        if self.size == 0:
            return "NULL"
        else:
            p = self.head
            s = []
            while p:
                s.append(str(p.val))
                p = p.next
            return " ".join(s)

class ListNode:
    def __init__(self, val, last, next):
        self.val = val
        self.last = last
        self.next = next

for i in range(int(input())):
    deque = LinkedList(None, None)
    for i in range(int(input())):
        t, p = map(int, input().split())
        if t == 1:
            deque.append(ListNode(p, deque.tail, None))
        elif deque.size != 0:
            if p == 0:
                deque.popleft()
            else:
                deque.pop()
    print(deque)

