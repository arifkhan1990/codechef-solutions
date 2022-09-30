for _ in range(int(input())):
    n ,s = map(int, input().split())

    if n >= s:
        print(s)
    else:
        print(n - (s-n))