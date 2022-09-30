for _ in range(int(input())):
    s = int(input())
    q = list(map(int,input(' ').strip().split()))[:s]
    
    eT = 0
    for i in range(s):
        e = list(map(int,input(' ').strip().split()))
        eT += sum(e[1:]) - (q[i]*(len(e) - 2))
    print(eT)

    