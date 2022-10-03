from sys import stdin
ip = stdin.readline
for _ in range(int(ip())):
    n , m = map(int,ip().split())
    ar = list(map(int,ip().split()))

    ar.sort()

    ans = float('inf')
    for i in range(n-m+1):
        if m+i - 1 < n and ar[m+i-1] - ar[i] < ans:
            ans = ar[m+i-1] - ar[i]

    print(ans)