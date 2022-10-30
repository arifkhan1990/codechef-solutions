dp = [False]*200001
for i in range(500):
    for j in range(i, 500):
        if i*i+j*j <= 200000:
            dp[i*i+j*j] = (i, j)


for _ in range(int(input())):
    
    n = int(input())
    cnt = 1
    while n%4==0:
        n //= 4
        cnt *= 2
    if dp[n] != False:
        print(dp[n][0]*cnt, dp[n][1]*cnt)
    else:
        print(-1)