from sys import stdin
ip = stdin.readline

for _ in range(int(ip())):
    n = int(ip())
    a = list(map(int,ip().split()))
    b = list(map(int,ip().split()))
    c = a.copy()
    c.sort()

    print('yes' if c==b else 'no')