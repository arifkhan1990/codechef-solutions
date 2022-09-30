for _ in range(int(input())):
    p = list(map(int, input().split()))
    p.sort()
    print(p[-1]+p[-2])