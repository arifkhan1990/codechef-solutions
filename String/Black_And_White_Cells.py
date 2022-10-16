from sys import stdin
ip = stdin.readline

for _ in range(int(ip())):
    s = input()
    if s == 'W':
      print('Chef')
    else:
      d = s
      print('Chef' if s == d[::-1] else 'Aleksa')