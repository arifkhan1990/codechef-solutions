from sys import stdin
ip = stdin.readline
for _ in range(int(ip())):
    n, k = map(int, ip().split())
    s = list(map(int,ip().split()))

    i = 0
    while 1:
        if i not in s and k == 0:
            print(i)
            break
        elif i not in s and  k > 0:
            k -=1
        i += 1
    