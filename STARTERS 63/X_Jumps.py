for _ in range(int(input())):
    x, y = map(int, input().split( ))
    z = x%y
    print((x//y)+z)