from sys import stdin
ip = stdin.readline

for _ in range(int(ip())):
    n = int(ip())
    ar = list(map(int,ip().split()))
    ans = [1]*n
    n -= 2
    
    while n >= 0:
        if ar[n]*ar[n+1] < 0:
            ans[n] += ans[n+1]
        n -= 1
    print(*ans)