from sys import stdin
ip = stdin.readline

for _ in range(int(ip())):
    s = ip()

    ans = 0
    res = 'Sad'
    for i in s:
        if ans > 2:
            res = 'Happy'
        if i in 'aeiou':
            ans += 1
        else:
            ans = 0
    print(res)
