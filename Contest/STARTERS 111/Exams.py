for _ in range(int(input())):
    x,y,z = map(int, input().split())

    if z > (x*y) // 2:
        print("YES")
    else:
        print("NO")