m = int(10e9+7)

def cla_func(n,x):
    c = 0
    while n > 0:
        c += n//x
        n /= x
    return c

def func(n, x):
    c = 0
    while n%x == 0:
        c += 1
        n /= x
    
    return c

b,a = map(int, input().split())

f = a-b
x = func(a,2)
y = func(b,5)

x1 = func(a,5)
y1 = func(b,2)

i , j = cla_func(a, 2), cla_func(a, 5)
k , l = cla_func(b, 2), cla_func(b, 5)
m , o = cla_func(f, 2), cla_func(f, 5)

ans = max(i-k-m+(x*y), j-l-o+(x1*y1))
print(ans)