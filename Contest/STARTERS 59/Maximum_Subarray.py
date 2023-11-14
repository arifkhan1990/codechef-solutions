from sys import stdin
ip = stdin.readline

for _ in range(int(ip())):
    n = int(ip())
    a = list(map(int,ip().split()))
    m = int(ip())
    b = list(map(int,ip().split()))

    ans = sum((x if x > 0 else 0 for x in b))

    mend = mfar = 0
    for i in range(n):
        mend += a[i]
        mfar = max(mfar,mend)
        mend = 0 if mend < 0 else mend
    print(mfar+ans)