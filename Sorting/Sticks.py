from sys import stdin
i_p = stdin.readline
for _ in range(int(i_p())):
    n = int(i_p())
    side = list(map(int,i_p().split()))
    
    side.sort(reverse=True)
    ans = i = 1
    l = 0
    while i < n and l != 2:
        if side[i] == side[i-1]:
            ans *= side[i]
            i += 2
            l += 1
        else:
            i += 1
    print(ans if l == 2 else -1)