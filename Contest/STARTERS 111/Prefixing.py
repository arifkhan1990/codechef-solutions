for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=[max(a)]*n 
    d={}
    for i in range(n):
        if a[i] not in d :
            d[a[i]]=i
    for i in d:
        b[d[i]]=i
    print(*b)