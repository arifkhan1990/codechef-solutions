from sys import stdin
ip = stdin.readline

for _ in range(int(ip())):
    n = int(ip())
    li = list(map(int,ip().split()))
    
    k = -1
    for i in range(n):
        if li[0] < li[i]:
            k = i
            break
    if k == -1:
        print(k)
    else:
        print(k)
        print(*li[:k])
        print(n-k)
        print(*li[k:])