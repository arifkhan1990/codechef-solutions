for _ in range(int(input())):
  n , k = map(int, input().split( ))
  ar = list(map(int, input().split( )))
  
  ar.sort()
  i = 0
  while i < len(ar):
    if ar[i] + ar[-1] <= k:
      ar.pop()
    else:
      i += 1
  print('NO' if len(ar) > 1 else 'YES')