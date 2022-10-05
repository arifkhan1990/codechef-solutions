from sys import stdin
ip = stdin.readline

for _ in range(int(ip())):
    n = int(ip())

    x = 1
    ans = 0
    while x <= n:
        if x&n == 0:
            ans += 1
        x <<= 1
    print(ans)