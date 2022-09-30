from sys import stdin
i_p = stdin.readline
for _ in range(int(i_p())):
    n, k = map(int, i_p().strip().split())
    ar = list(map(int,i_p().strip().split()))[:n]
    ar.sort()
    sm = 0
    for i in range(n):
        if k == i:
            break
        elif ar[i] < 0:
            ar[i] *= -1
    for x in ar:
        if x > 0:
            sm += x
    print(sm)