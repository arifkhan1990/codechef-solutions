from sys import stdin
ip = stdin.readline
from collections import Counter
for _ in range(int(ip())):
    n = int(ip())
    ar = list(map(int,ip().split()))
    ar.sort()
    ans = 0
    res = ''
    for i in range(0,n):
        if ar[i] > i+1:
            res = 'Second'
            break
        else:
            ans += (i+1) - ar[i]
    if res != '':
        print(res)
    else:
        res = 'Second' if ans%2 == 0 else 'First'
        print(res)


