def gcd(a, b):
    if b == 0:
        return abs(a)
    else:
        return gcd(b, a%b)

def lcm(a, b):
    return (a*b)//gcd(a,b)

from collections import Counter

T = int(input())
for i in range(T):
    n = int(input())
    arr = list(map(int,input(' ').strip().split()))[:n]
    ans = 0
    ar = Counter(arr)
    val = list(ar.values())
    for x in val:
        if x > 1:
            ans += (x * (x-1))//2
    print(ans)