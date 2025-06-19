import heapq

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr += 1
    for _ in range(T):
        m = int(input[ptr])
        n = int(input[ptr+1])
        ptr += 2
        sequences = []
        for _ in range(m):
            seq = list(map(int, input[ptr:ptr+n]))
            ptr += n
            seq.sort()
            sequences.append(seq)
        prev_sums = sequences[0].copy()
        for i in range(1, m):
            print(prev_sums)
            curr = sequences[i]
            heap = []
            for i_prev in range(n):
                s = prev_sums[i_prev] + curr[0]
                heapq.heappush(heap, (s, i_prev, 0))
            new_sums = []
            while len(new_sums) < n and heap:
                print(heap)
                s, i_prev, j_curr = heapq.heappop(heap)
                new_sums.append(s)
                if j_curr + 1 < n:
                    next_j = j_curr + 1
                    next_s = prev_sums[i_prev] + curr[next_j]
                    heapq.heappush(heap, (next_s, i_prev, next_j))
                    
            prev_sums = new_sums
        print(' '.join(map(str, prev_sums)))

if __name__ == "__main__":
    main()