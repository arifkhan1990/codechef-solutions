for _ in range(int(input())):
    n , k = map(int,input().split())
    ar = list(map(int,input().split()))
    sm = sum(ar)
    for _ in range(k):
        x, y = map(int, input().split( ))
        b = (y-x) + 1
        if b&1 == 1:
            sm += (b//2) + 1
        else:
            sm += b//2
        sm -= (b//2)
    print(sm)
