for _ in range(int(input())):
    a,b,c,d,k = map(int, input().split())

    move = abs(a-c) + abs(b-d)

    if move == k or (k > move and (k-move)%2 == 0):
        print('YES')
    else:
        print('NO')