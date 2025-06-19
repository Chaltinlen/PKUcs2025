class heap:
    def __init__(self):
        self.L = []
    def heappush(self, u):
        self.L.append(u)
        ind = len(self.L) - 1
        head = (ind - 1) // 2
        while ind and self.L[ind] < self.L[head]:
            oth = 4 * ((head - 1) // 2) - head + 3
            if head and self.L[head] < self.L[oth]:
                self.L[head], self.L[oth] = self.L[oth], self.L[head]
            self.L[ind], self.L[head] = self.L[head], self.L[ind]
            ind = head
            head = (ind - 1) // 2
    def heappop(self):
        ind = len(self.L) - 1
        path = []
        while ind:
            path.append(ind)
            ind = (ind - 1) // 2
        path.reverse()
        ind = 0
        for sub in path:
            oth = 4 * ind - sub + 3
            if oth < len(self.L) and self.L[sub] > self.L[oth]:
                self.L[sub], self.L[oth] = self.L[oth], self.L[sub]
                while True:
                    a = (2 * oth + 2 < len(self.L) - 1) and self.L[oth] > self.L[2 * oth + 2]
                    b = (2 * oth + 1 < len(self.L) - 1) and self.L[oth] > self.L[2 * oth + 1]
                    if a:
                        self.L[oth], self.L[2 * oth + 2] = self.L[2 * oth + 2], self.L[oth]
                        c = 2 * oth + 2
                    if b:
                        self.L[oth], self.L[2 * oth + 1] = self.L[2 * oth + 1], self.L[oth]
                        c = 2 * oth + 1
                    if a or b:
                        oth = c
                    else:
                        break

            self.L[ind], self.L[sub] = self.L[sub], self.L[ind]
            ind = sub
        return self.L.pop()

h = heap()
for i in range(int(input())):
    p = input().split()
    if len(p) == 1:
        print(h.heappop())
    else:
        h.heappush(int(p[1]))
