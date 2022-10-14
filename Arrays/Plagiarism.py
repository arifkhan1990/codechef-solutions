from sys import stdin
ip = stdin.readline
for _ in range(int(ip())):
    n , m, k = map(int, input().split())
    quize = list(map(int,ip().split()))
    user = [0]*(n+1)
    ans = []
    for i in quize:
        if i <= n:
            user[i-1] += 1
    for i,x in enumerate(user):
        if x > 1:
            ans.append(i+1)
    print(len(ans), *ans)
