from sys import stdin
ip = stdin.readline

for _ in range(int(ip())):
    a,b = map(int, ip().split())
    print(a+b)