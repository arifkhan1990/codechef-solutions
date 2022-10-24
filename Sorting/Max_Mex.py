from sys import stdin
ip = stdin.readline
from collections import Counter
for _ in range(int(ip())):
    n, k = map(int, ip().split())
    s = set(list(map(int,ip().split())))
    
    i = 0

    while 1:
        if i not in s and k == 0:
            break
        elif i not in s and  k > 0:
            k -=1
        i += 1
    print(i)
    t = int(input())
