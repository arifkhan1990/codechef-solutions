from sys import stdin
ip = stdin.readline
from operator import itemgetter
for _ in range(int(ip())):
    n , m, x = map(int, ip().split())
    li = list(map(int,ip().split()))
    ad = [(i+1, li[i]) for i in range(n) ]
    ad = sorted(ad, key=itemgetter(1))
    ad = ad[::-1]
    ans = []
    for i in ad:
        if i[1] >= m:
            ans.append(i[0])
        elif len(ans) < x:
            ans.append(i[0])
    ans.sort()
    print(len(ans), *ans, sep = ' ')

