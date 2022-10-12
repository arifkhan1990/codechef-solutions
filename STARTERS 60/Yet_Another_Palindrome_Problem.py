from sys import stdin
ip = stdin.readline
from collections import Counter
for _ in range(int(ip())):
    n = int(ip())
    ar = list(map(int,ip().split()))
    ans = 0
    for i in reversed(range(n//2)):
        ar[i] += ans
        if ar[i] > ar[n-1-i]:
            ans = -1
            break
        ans += ar[n-1-i] - ar[i]
    print(ans)
