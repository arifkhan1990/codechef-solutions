for _ in range(int(input())):
    s = input()
    l_ok = u_ok = s_ok = d_ok = len_ok = 0
    l = len(s)
    for i in range(l):
        if s[i] in 'abcdefghijklmnopqrstuvwxyz':
            l_ok = 1
        elif s[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' and i != 0 and i != l-1:
            u_ok = 1
        elif s[i] in '0123456789' and i != 0 and i != l-1:
            d_ok = 1
        elif s[i] in ['@', '#', '%', '&', '?'] and i != 0 and i != l-1:
            s_ok = 1
    if l >= 10:
        len_ok = 1

    print('YES' if l_ok & d_ok & u_ok & s_ok & len_ok else 'NO')