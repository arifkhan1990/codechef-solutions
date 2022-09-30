for _ in range(int(input())):
    n = int(input())
    li = list(map(int,input(' ').strip().split()))[:n]
    li.sort()
    d = max(li[0], li[n//2])
    print(n - li.index(d))