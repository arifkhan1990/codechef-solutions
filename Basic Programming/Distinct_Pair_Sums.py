for _ in range(int(input())):
    a,b = map(int, input().split())
    mx = max(a,b)
    mi = min(a,b)
    print(2*mx - 2*mi + 1)