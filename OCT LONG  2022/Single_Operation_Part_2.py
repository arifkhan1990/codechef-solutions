from sys import stdin
ip = stdin.readline
for _ in range(int(ip())):
    n = int(ip())
    s = ip()
    ans = 1
    for i in range(1,n):
        if s[i] == '1':
            break
        else:
            ans += 1
    print(ans)
    