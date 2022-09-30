for _ in range(int(input())):
    n, p, x, y = map(int, input().split(' '))
    li = list(map(int, input().split()))
    
    for i in range(n):
        if li[i] == 1:
            li[i] = y
        else:
            li[i] = x
    print(sum(li[:p]))