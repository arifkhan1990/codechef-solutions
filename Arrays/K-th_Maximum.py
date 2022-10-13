from sys import stdin
ip = stdin.readline
from collections import Counter
for _ in range(int(ip())):
    n,k = map(int,ip().split())
    ar = list(map(int,ip().split()))
    ans = 0
    mx = max(ar)
    for i, x in enumerate(ar):
        if x == mx:
            if i - k + 1 >= 0:
                ans += n - i
    print(ans)



