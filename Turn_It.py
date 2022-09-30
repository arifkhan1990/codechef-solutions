for _ in range(int(input())):
    u,v,a,s = map(int, input().split())

    if v*v < u*u - 2*a*s:
        print('No')
    else:
        print('Yes')