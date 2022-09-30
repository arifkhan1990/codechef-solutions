for _ in range(int(input())):
    m ,x, y = map(int, input().split(' '))
    cops = list(map(int,input(' ').strip().split()))

    n = x*y
    s = [0]*101

    for i in range(m):
        p = 1 if cops[i] - n <= 1 else cops[i]-n
        q = 100 if cops[i]+n > 100 else cops[i]+n 
        for j in range(p,q+1):
            s[j] = 1

    print(s.count(0)-1)