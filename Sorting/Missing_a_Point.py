from sys import stdin
ip = stdin.readline
for _ in range(int(ip())):
    n = int(ip())
    ans_x = ans_y = 0
    for i in range(4*n - 1):
        x,y = map(int, ip().split(' '))

        ans_x ^= x
        ans_y ^= y
    print(ans_x, ans_y)