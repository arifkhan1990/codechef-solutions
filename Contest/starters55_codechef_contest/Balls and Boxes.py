T = int(input())
for _ in range(T):
  x, y = map(int, input().split(' '))
  if x < y:
      print('NO')
  else:
    if x >= (y*(y+1))//2:
      print('YES')
    else:
      print('NO')