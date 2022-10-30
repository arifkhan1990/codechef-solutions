for _ in range(int(input())):
    n = int(input())
    x = n//2
    h = 4 * (x * (x+1) * (2 * x + 1) // 6)
    w = n * (n+1) * (2 * n + 1) // 6
    print(w - h if n&1 == 1 else h)