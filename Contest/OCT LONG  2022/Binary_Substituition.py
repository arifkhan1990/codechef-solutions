from sys import stdin
ip = stdin.readline
mod = 998244353
    
for _ in range(int(ip())):
    s = input()
    n = len(s)
    res = [1]*(n+1)
    for i in range(1,n):
        res[i+1] = res[i]
        if s[i] != s[i-1]:
            res[i+1] += res[i-1]
        res[i+1] %= mod
    print(res[n])