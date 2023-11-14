from sys import stdin
ip = stdin.readline
from collections import Counter
for _ in range(int(ip())):
    n = map(int, ip().split())
    s = ip()
    zC = s.count('0')
    oC = s.count('1')

    print('YES' if (zC%2)&(oC%2) == 0 else 'NO')

