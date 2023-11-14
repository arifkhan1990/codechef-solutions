
for _ in range(int(input())):
    n , k = map(int, input().split())
    print('YES' if n*2 <= k or n == k else 'NO')