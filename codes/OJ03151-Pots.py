from collections import deque

a, b, c = map(int, input().split())

def bfs():
    queue = deque()
    queue.append((0, 0, []))
    visited = set()
    visited.add((0, 0))

    while queue:
        v1, v2, path = queue.popleft()
        if v1 == c or v2 == c:
            return path
        
        # FILL(1)
        if v1 < a and (a, v2) not in visited:
            queue.append((a, v2, path + ['FILL(1)']))
            visited.add((a, v2))

        # FILL(2)
        if v2 < b and (v1, b) not in visited:
            queue.append((v1, b, path + ['FILL(2)']))
            visited.add((v1, b))

        # DROP(1)
        if v1 > 0 and (0, v2) not in visited:
            queue.append((0, v2, path + ['DROP(1)']))
            visited.add((0, v2))

        # DROP(2)
        if v2 > 0 and (v1, 0) not in visited:
            queue.append((v1, 0, path + ['DROP(2)']))
            visited.add((v1, 0))

        # POUR(1,2)
        if v1 > 0 and v2 < b:
            pour_to_2 = min(v1, b - v2)
            new_v1 = v1 - pour_to_2
            new_v2 = v2 + pour_to_2
            if (new_v1, new_v2) not in visited:
                queue.append((new_v1, new_v2, path + ['POUR(1,2)']))
                visited.add((new_v1, new_v2))

        # POUR(2,1)
        if v2 > 0 and v1 < a:
            pour_to_1 = min(v2, a - v1)
            new_v1 = v1 + pour_to_1
            new_v2 = v2 - pour_to_1
            if (new_v1, new_v2) not in visited:
                queue.append((new_v1, new_v2, path + ['POUR(2,1)']))
                visited.add((new_v1, new_v2))

    return None

ans = bfs()
if ans:
    print(len(ans))
    for step in ans:
        print(step)
else:
    print('impossible')