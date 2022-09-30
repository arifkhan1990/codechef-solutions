for _ in range(int(input())):
    s = input()

    fS = s[0:len(s)//2]
    sS = s[len(s)//2 if len(s)%2 == 0 else (len(s)//2)+1:len(s)]
    print('YES' if sorted(fS) == sorted(sS) else 'NO')