for _ in range(int(input())):
  a = input() + '00'
  b = input() + '00'
  ans = 0
  i = 0
  while i < len(a):
    if a[i] != b[i]:
      if a[i+2] == b[i+2]:
        ans += 1
    i += 1
  print(ans)