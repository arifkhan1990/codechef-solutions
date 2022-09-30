for _ in range(int(input())):
    n , m = map(int, input().split())
    x, y = map(int, input().split(' '))
    ans = ''
    for _ in range(n):
        s = input()
        f = s.count('F')
        p = s.count('P')
        if f  >= x or (f == x-1 and p >= y):
            ans += '1'
        else:
            ans += '0'
    print(ans)
