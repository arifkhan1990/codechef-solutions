s = input()
for _ in range(int(input())):
    w = input()
    ok = 1
    for c in w:
        if c not in s:
            ok = 0
    print('Yes' if ok == 1 else 'No')