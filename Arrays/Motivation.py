t = int(input())

for _ in range(t):
  n, x = map(int, input().split( ))
  ans = 0
  for i in range(n):
    si, ri = map(int, input().split( ))
    if si <= x:
      ans = max(ans, ri)
  print(ans)  