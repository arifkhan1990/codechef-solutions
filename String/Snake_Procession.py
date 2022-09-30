for _ in range(int(input())):
    l = int(input())
    s = input()
    valid = 1
    for i in s:
        if i == 'H':
            if valid:
                valid = 0
            else:
                valid = 0
                break
        elif i == 'T':
            if valid == 0:
                valid = 1
            else:
                valid = 0
                break
    print('Valid' if valid == 1 else 'Invalid')