from sys import stdin
i_p = stdin.readline

for _ in range(int(i_p())):
    n = int(i_p())
    digit = ['0']*n
    digit[0] = digit[n-1] = '3'
    print(''.join(digit))