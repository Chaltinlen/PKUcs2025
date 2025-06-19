from collections import defaultdict
commits = defaultdict(lambda: [set(), 0])
for i in range(int(input())):
    univ, question, status = input().split(",")
    if status == "yes":
        commits[univ][0].add(question)
    commits[univ][1] += 1
rate = sorted(commits, key=lambda t: (-len(commits[t][0]), commits[t][1], t))[:12]
for i in range(len(rate)):
    print(i + 1, rate[i], len(commits[rate[i]][0]), commits[rate[i]][1])