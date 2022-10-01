from sys import stdin
i_p = stdin.readline
for _ in range(int(i_p())):
    a,b,p,q = map(int, i_p().split())
    if (a*1 == p or a == p) and (b*2 == q or b == q):
        print('YES')
    else:
        print('NO')
    # print('YES' if p%a == 0 and q%b == 0 else 'NO')