from cgitb import reset
from sys import stdin
ip = stdin.readline
from collections import Counter
for _ in range(int(ip())):
    n = int(ip())
    s = list(map(int,ip().split()))
    res = []
    ans = 0

    for i in range(n):
        if len(res) == 0:
            res.append(s[i])
        else:
            if s[i] != res[-1]:
                ans += 1
                res.pop()
            else:
                res.append(s[i])
    while len(res) >= 2:
        tp = res[-1]
        res.pop()
        if tp == res[-1]:
            res.pop()
            res.append(0)
        else:
            ans += 1
            res.pop()
    print(ans)