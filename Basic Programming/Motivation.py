for _ in range(int(input())):
    n , x = map(int, input().split())
    mx = 0
    for i in range(n):
        s,r = map(int, input().split())
        if s <= x:
            mx = max(mx, r)
    print(mx)

