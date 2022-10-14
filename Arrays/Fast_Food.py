from sys import stdin
ip = stdin.readline
for _ in range(int(ip())):
    n = int(ip())
    ar = list(map(int,ip().split()))
    br = list(map(int,ip().split()))
    sm = cSm = sum(br)
    for i in range(n):
        cSm = cSm - br[i] + ar[i]
        sm = max(sm,cSm)
    print(sm)