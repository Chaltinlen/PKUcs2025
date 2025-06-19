class doubleLinkedList:
    def __init__(self, val, last, next):
        self.val = val
        self.last = last
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.pair = {}
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.pair:
            if self.pair[key].next:
                if not self.pair[key].last:
                    self.head = self.head.next
                    self.head.last = None
                else:
                    self.pair[key].last.next = self.pair[key].next
                    self.pair[key].next.last = self.pair[key].last
                self.pair[key].last = self.tail
                self.pair[key].next = None
                self.tail.next = self.pair[key]
                self.tail = self.tail.next
            return self.pair[key].val[1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.pair:
            self.pair[key].val = (key, value)
            if self.pair[key].next:
                if not self.pair[key].last:
                    self.head = self.head.next
                    self.head.last = None
                else:
                    self.pair[key].last.next = self.pair[key].next
                    self.pair[key].next.last = self.pair[key].last
                self.pair[key].last = self.tail
                self.pair[key].next = None
                self.tail.next = self.pair[key]
                self.tail = self.tail.next
        else:
            self.size += 1
            if self.size == 1:
                
                self.pair[key] = doubleLinkedList((key, value), None, None)
                self.head = self.tail = self.pair[key]
            else:
                self.pair[key] = doubleLinkedList((key, value), self.tail, None)
                self.tail.next = self.pair[key]
                self.tail = self.tail.next
                if self.size > self.capacity:
                    self.pair.pop(self.head.val[0])
                    self.head = self.head.next
                    self.head.last = None
                    
                    self.size = self.capacity


if __name__ == '__main__':
    input = [["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"], [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]]
    lru = None
    for i in range(len(input[0])):
        if input[0][i] == "LRUCache":
            lru = LRUCache(input[1][0][0])
        elif input[0][i] == "put":
            print(f"put({input[1][i][0]}, {input[1][i][1]})")
            lru.put(input[1][i][0], input[1][i][1])
        elif input[0][i] == "get":
            print(f"get({input[1][i][0]})")
            print(lru.get(input[1][i][0]))




