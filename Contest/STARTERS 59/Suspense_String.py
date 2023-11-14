from sys import stdin
ip = stdin.readline

for _ in range(int(ip())):
    n = int(ip())
    s = ip()

    t = []
    i = 0
    a = 0
    j = n-1
    while i <= j:
        if a == 0:
            if s[i] == '0':
                t = ['0', *t]
            else:
                t = [*t, '1']
            a , i = 1, i+1
        else:
            if s[j] == '0':
                t = [*t, '0']
            else:
                t = ['1', *t]
            a , j = 0, j-1
    print(''.join(t))
        