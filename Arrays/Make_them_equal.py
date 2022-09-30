for _ in range(int(input())):
    n = int(input())
    li = list(map(int,input(' ').strip().split()))[:n]
    li.sort()
    print(li[-1] - li[0])