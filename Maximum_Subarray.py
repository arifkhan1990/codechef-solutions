from sys import stdin
ip = stdin.readline

for _ in range(int(ip())):
    n = int(ip())
    a = list(map(int,ip().split()))
    m = int(ip())
    b = list(map(int,ip().split()))

    ans = []
    for i in range(n):
        if a[i] >= 