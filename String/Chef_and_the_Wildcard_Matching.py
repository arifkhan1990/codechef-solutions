for _ in range(int(input())):
    x = list(input())
    y = list(input())

    for i in range(len(x)):
        if x[i] == '?' and y[i] != '?':
            x[i] = y[i]
        elif x[i] != '?' and y[i] == '?':
            y[i] = x[i]

    x = ''.join(x)
    y = ''.join(y)

    print('Yes' if  x == y else 'No')