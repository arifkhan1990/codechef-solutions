from sys import stdin
ip = stdin.readline
for _ in range(int(ip())):
    n = int(ip())
    colorSet= set(map(int,ip().split()))
    print(0 if n == len(colorSet) else n-len(colorSet))