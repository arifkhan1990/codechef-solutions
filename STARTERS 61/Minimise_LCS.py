from sys import stdin
ip = stdin.readline
from collections import Counter
for _ in range(int(ip())):
    n = int(ip())
    a = input()
    b = input()

    c = Counter(a)
    d = Counter(b)
    # print(c,d)
    ans = []
    for i in c:
        if i in d:
            x = min(c[i],d[i])
            ans.append(x)
    print(0 if len(ans) == 0 else max(ans))