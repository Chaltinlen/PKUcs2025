from sys import stdin, stdout
get = stdin.read().split("\n")
for line in get:
    out = []
    cnt = 0
    leftbr = []
    for i in range(len(line)):
        if line[i] == "(":
            out.append(" ")
            leftbr.append(i)
        elif line[i] == ")":
            if leftbr:
                leftbr.pop()
                out.append(" ")
            else:
                out.append("?")
        else:
            out.append(" ")
    while leftbr:
        out[leftbr.pop()] = "$"
    print(line + "\n" + "".join(out))
