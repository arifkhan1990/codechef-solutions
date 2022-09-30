for _ in range(int(input())):
    n, m ,k = map(int, input().split())
    li = list(map(int, input().split()))

    if n == sum(li):
        print(100)
    elif m <= sum(li[:m]):
        print(k)
    else:
        print(0)