for _ in range(int(input())):
    n , a,b = map(int, input().split())
    sak =  anu = 0
    for i in range(n):
        s = input()
        if s[0] in 'EQUINOX':
            sak += a
        else:
            anu += b
    if sak > anu:
        print('SARTHAK')
    elif sak < anu:
        print('ANURADHA')
    else:
        print('DRAW')