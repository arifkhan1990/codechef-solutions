from bisect import bisect, insort
n ,q = map(int,input().split())
ar = list(map(int,input().split()))
ar.sort()

for _ in range(q):
    x = int(input())
    k = bisect(ar, x)
    if ar[k - 1] == x:
        print(0)
    elif (n-k)&1 == 1:
        print('NEGATIVE')
    else:
        print('POSITIVE')