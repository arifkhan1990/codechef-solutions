for _ in range(int(input())):
    a,b,a1,b1,a2,b2 = map(int, input().split())
    l1 = [a1,b1]
    l2 = [a2,b2]
    if a in l1 and b in l1:
        print(1)
    elif a in l2 and b in l2:
        print(2)
    else:
        print(0)