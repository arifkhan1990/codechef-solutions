for _ in range(int(input())):
    d, l, r = map(int, input().split())

    if d > r:
        print('Too Late')
    elif d < l:
        print('Too Early')
    else:
        print('Take second dose now')