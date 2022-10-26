
for _ in range(int(input())):
    n = int(input())
    a = 0
    while n%2 == 0:
        a += 1
        n //= 2
    
    if a%2 == 1:
        a -= 1
        n *= 2
    
    i = 0
    c,d = 0, 0
    while i*i <= n:
        y = n - (i*i)
        b = math.sqrt(y)
        if b *b == y:
            c,d = b << (a//2), 1 << (a//2)
            break
    if c == 0 and d == 0:
        print(-1)
    else:
        print(c,d)