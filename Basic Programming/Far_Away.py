for _ in range(int(input())):
    n , m = map(int, input().split())
    nums = list(map(int,input(' ').strip().split()))[:n]
    ans = 0

    for i in nums:
        if i <= m//2:
            ans += abs(i - m)
        else:
            ans += abs(i - 1)
    print(ans)