from sys import stdin
i_p = stdin.readline
for _ in range(int(i_p())):
    dif = list(map(int,i_p().strip().split()))
    k = int(i_p())
    ans = 0

    for i in range(9,-1, -1):
        if dif[i] - k > 0:
            ans = i+1
            break
        else:
            k -= dif[i]
    print(ans)
        

