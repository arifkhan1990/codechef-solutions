from sys import stdin
i_p = stdin.readline
for _ in range(int(i_p())):
    n ,k = map(int,i_p().split())
    p = list(map(int,i_p().split()))

    ans = float('inf')
    pos = -1
    for i in p:
        if k%i == 0:
            if ans > k//i:
                ans = k//i
                pos = i
    print(pos)