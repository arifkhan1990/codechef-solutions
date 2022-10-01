from sys import stdin
i_p = stdin.readline
for _ in range(int(i_p())):
    n ,x = map(int, i_p().split())
    coch = set(map(int, i_p().strip().split()))

    s_e = n - x
    l =  len(coch)
    print(s_e if l > s_e else l)
