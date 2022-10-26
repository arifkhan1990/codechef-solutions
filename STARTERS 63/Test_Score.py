for _ in range(int(input())):
    n, x ,y = map(int, input().split())
    print('YES' if y%x == 0 else 'NO')