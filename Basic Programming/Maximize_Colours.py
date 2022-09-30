for _ in range(int(input())):
    x, y, z = map(int, input().split())

    ans = 0

    if x > 0:
        ans += 1

    if y > 0:
        ans += 1

    if z > 0:
        ans += 1
    s = [x,y,z]
    s.sort()
    x,y,z = s[0],s[1],s[2]
    if x == 2:
        ans += 2 if z >= 3 else 1
    elif x >= 3:
        ans += 3
    elif y <= 1:
        ans = ans
    else:
        ans += 1

    print(ans)
    
