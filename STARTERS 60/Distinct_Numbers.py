from sys import stdin
ip = stdin.readline
from collections import Counter
for _ in range(int(ip())):
    n , k= map(int, ip().split())
    ar = list(map(int,ip().split()))
    dp = [0]*(2*n+1)
    for i in ar:
        dp[i] = 1
    b = []
    for i in range(1, 2*n+1):
      if dp[i] == 0:
        b.append(i)
    mx = max(ar)
    ans = float('-inf')
    ans = max((k-1)*(2*n) - sum(b[:k-1]), (k*mx - sum(b[:k])))
    print(ans)