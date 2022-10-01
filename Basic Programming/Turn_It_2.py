from sys import stdin
i_p = stdin.readline
for _ in range(int(i_p())):
    u,v,a,s = map(int, i_p().split())
    print('No' if v*v < u*u - 2*a*s else 'Yes')