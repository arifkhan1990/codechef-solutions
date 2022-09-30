from sys import stdin
i_p = stdin.readline
for _ in range(int(i_p())):
    n = int(i_p())
    ar = list(map(int,i_p().strip().split()))[:n]
    ar.sort()
    print(ar[0]+ar[1])