from sys import stdin
ip = stdin.readline
from collections import Counter
for _ in range(int(ip())):
    s = input()
    b = input()
    c = Counter(s)
    for i in b:
        c[i] -= 1
    a = x = ''

    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i == b[0]:
            x += b
        a += i*c[i]
        x += i*c[i]
        if i == b[0]:
            a += b
    print(a if a < x else x)