for _ in range(int(input())):
    n = int(input())
    li = list(map(int,input(' ').strip().split()))[:n]
    ans = 1
    for i in range(1,n):
        if  li[i] <= li[i-1]:
            ans += 1
        else:
            li[i] = li[i-1]
    
    print(ans)