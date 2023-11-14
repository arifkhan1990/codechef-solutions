from sys import stdin
ip = stdin.readline
for _ in range(int(ip())):
    a , b, c = map(int, input().split())
    sm = a+b+c
    if (sm-a)%2:
        print("YES")
    elif (sm-b)%2:
        print("YES")
    elif (sm-c)%2:
        print("YES")
    else:
        print("NO")