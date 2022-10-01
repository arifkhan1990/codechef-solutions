from sys import stdin
i_p = stdin.readline
for _ in range(int(i_p())):
    n , m = map(int, i_p().split())
    print((m-n)*2 +1)