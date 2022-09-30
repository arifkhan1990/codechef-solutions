for _ in range(int(input())):
    n , k = map(int, input().split())
    li = list(map(int,input().split()))
    ans = 0
    for i in li:
        ans += i%k
    print(ans%k)