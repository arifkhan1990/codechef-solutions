from sys import stdin
i_p = stdin.readline
for _ in range(int(i_p())):
    n , k = map(int, i_p().split())
    w = list(map(int,i_p().split()))

    w.sort()
    g1 = abs(sum(w[k:n]) - sum(w[:k]))
    g2 = abs(sum(w[n-k:]) - sum(w[:n-k]))
    print(g1 if g2 < g1 else g2)