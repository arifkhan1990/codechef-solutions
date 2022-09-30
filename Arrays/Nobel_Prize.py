for _ in range(int(input())):
    n , m = map(int, input().split())
    rec = set(list(map(int, input().split())))
    print('Yes' if m > len(rec) else 'No')

