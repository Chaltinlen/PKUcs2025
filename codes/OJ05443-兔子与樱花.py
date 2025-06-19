place = []
place_to_num = {}
P = int(input())
D = [[0 for i in range(P)] for j in range(P)]
f = [[[0, [x]] if x == y else [1e9, []] for x in range(P)] for y in range(P)]
for i in range(P):
    place.append(input())
    place_to_num[place[-1]] = i
for i in range(int(input())):
    p1, p2, d = input().split()
    p1, p2, d = place_to_num[p1], place_to_num[p2], int(d)
    f[p1][p2] = [d, [p1, p2]]
    f[p2][p1] = [d, [p2, p1]]
    D[p1][p2] = D[p2][p1] = d
for k in range(P):
    for x in range(P):
        for y in range(P):
             if f[x][k][0] + f[k][y][0] < f[x][y][0]:
                f[x][y] = [f[x][k][0] + f[k][y][0], f[x][k][1] + f[k][y][1][1:]]
for i in range(int(input())):
    scr, des = input().split()
    stt, end = place_to_num[scr], place_to_num[des]
    print(scr, end="")
    mat = f[stt][end][1]
    for i in range(1, len(mat)):
        print(f"->({D[mat[i-1]][mat[i]]})->{place[f[stt][end][1][i]]}", end="")
    print()
