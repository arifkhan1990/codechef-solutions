from sys import stdin
ip = stdin.readline
from collections import Counter
for _ in range(int(ip())):
    n,k = map(int, ip().split())
    ans = n//k
    print(ans*ans)

