
n,m,k = map(int, input().split())
ans = 0
for i in range(n):
    li = list(map(int,input().split()))
    
    if m <= sum(li[:-1]) and li[-1] <= 10:
        ans += 1

print(ans)