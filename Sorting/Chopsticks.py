from sys import stdin
i_p = stdin.readline
n ,d = map(int, i_p().split())
ar = []
for i in range(n):
    ar.append(int(i_p()))
ar.sort()
ans = 0 
i = 1
while(i < n):
    if ar[i] - ar[i-1] <= d:
        ans += 1
        i += 2
    else:
        i += 1
print(ans)
    