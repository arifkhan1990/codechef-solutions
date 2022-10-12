from sys import stdin
ip = stdin.readline
for _ in range(int(ip())):
    a,b,x,y = map(int, ip().split(' '))
    if a/x < b/y:
        print('Chef')
    elif a/x > b/y:
        print('Chefina')
    else:
        print('Both')