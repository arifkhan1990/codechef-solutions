from sys import stdin
ip = stdin.readline
for _ in range(int(ip())):
    n = int(ip())
    s = input()

    ans = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            ans += 1
    print(ans)
