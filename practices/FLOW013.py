T = int(input())
for i in range(T):
  a, b, c = map(int, input().split())
  
  print('YES' if a+b+c == 180 else 'NO')