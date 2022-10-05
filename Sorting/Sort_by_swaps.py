from sys import stdin
ip = stdin.readline
n = int(ip())
ar = list(map(int,ip().split()))

idx = []
for i in range(n):
    k = i
    for j in range(i,n):
        if ar[j] < ar[k]:
            k = j
    if k != i:
        ar[k], ar[i] = ar[i], ar[k]
        idx.append((i,k))

print(len(idx))
for i in range(len(idx)):
    print(idx[i][0], idx[i][1])
