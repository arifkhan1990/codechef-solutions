from sys import stdin
i_p = stdin.readline
for _ in range(int(i_p())):
    n = int(i_p())
    ar = [str(i) for i in range(1,n+1)]
    i = 0
    while i < n-1:
        ar[i] , ar[i+1] = ar[i+1], ar[i]
        i += 2
    if n%2 == 1:
        ar[0], ar[n-1] = ar[n-1], ar[0]
    print(' '.join(ar))
