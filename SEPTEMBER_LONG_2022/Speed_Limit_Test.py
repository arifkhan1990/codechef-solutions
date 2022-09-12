T = int(input())
for i in range(T):
    a,b,x, y = map(int, input().split(' '))
    if a/x > b/y :
        print('Alice')
    elif a/x < b/y:
        print('Bob')
    else:
        print('Equal')