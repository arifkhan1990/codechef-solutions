for _ in range(int(input())):
    n = int(input())
    li = list(map(int,input(' ').strip().split()))[:n]
    ballon = []
    
    i = 0
    while len(ballon) < 7:
        if li[i] > 0 and li[i] < 8:
            ballon.append(li[i])
        i += 1
    print(i)