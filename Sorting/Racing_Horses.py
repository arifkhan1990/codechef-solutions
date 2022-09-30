from sys import stdin
i_p = stdin.readline
for _ in range(int(i_p())):
    n = int(i_p())
    ar = list(map(int,i_p().strip().split()))[:n]
    ar.sort()
    mi = float('inf')
    for i in range(1,n):
        if mi > ar[i] - ar[i-1]:
            mi = ar[i] - ar[i-1]
    print(mi)