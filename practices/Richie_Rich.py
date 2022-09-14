T = int(input())
for _ in range(T):
    a,b,x = map(int, input().split())

    print((b-a)//x + (b-a)%x)