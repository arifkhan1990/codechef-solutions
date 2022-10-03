from sys import stdin
ip = stdin.readline
from collections import Counter
for _ in range(int(ip())):
    n = int(ip())
    li = list(map(int,ip().split()))
    if n <= 2:
        print(0)
    else:
        f = Counter(li)
        print(min(n-2, n - max(f.values())))