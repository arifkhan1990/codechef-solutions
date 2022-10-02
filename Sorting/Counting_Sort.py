# cook your dish here
from sys import stdin
ip = stdin.readline

for _ in range(int(ip())):
    n = int(ip())
    ar = list(map(int,ip().split()))
    
    mx = max(ar) + 1
    count = [0]*mx

    for i in range(0,n):
        count[ar[i]] += 1
    
    for i in range(1,mx):
        count[i] += count[i-1]

    l = n-1
    output = [0]*mx
    while l >= 0:
        output[count[ar[l]]-1] = ar[l]
        count[ar[l]] -= 1
        l -= 1
    res =[str(x) for x in output[0:n]]

    print(' '.join(res))