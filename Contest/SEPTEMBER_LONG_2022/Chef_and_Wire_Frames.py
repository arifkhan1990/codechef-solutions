T = int(input())
for i in range(T):
    n, m, x = map(int, input().split())
    print((n*2 + m*2) * x)