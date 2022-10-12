from sys import stdin
ip = stdin.readline
for _ in range(int(ip())):
    n = int(ip())
    s = ip()
    ans = 0
    for i in s:
        if i == '1':
            ans += 1
        else:
            break
    print(ans)
    