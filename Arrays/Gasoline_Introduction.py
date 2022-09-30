for _ in range(int(input())):
    n = int(input())
    li = list(map(int,input(' ').strip().split()))[:n]
    ans = k = 0

    for i in li:
        if i == 0:
            if ans == 0:
                break
        else:
            ans += i
        ans -= 1
        k += 1
        # print(ans)
    print(ans+k)