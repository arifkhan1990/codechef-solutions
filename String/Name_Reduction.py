from sys import stdin
ip = stdin.readline
from collections import Counter

for _ in range(int(ip())):
    a, b = input().split(' ')
    n = int(ip())
    ch = ''
    for i in range(n):
        s = input()
        ch += s
    c = Counter(a+b)
    d = Counter(ch)

    ans = 1
    for i in d:
        if i in c:
            if d[i] > c[i]:
                ans = 0
                break
        else:
            ans = 0
            break
    print('YES' if ans == 1 else 'NO')