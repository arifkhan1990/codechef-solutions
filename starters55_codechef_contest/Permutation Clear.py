T = int(input())
for i in range(T):
  n = int(input())
  a = list(map(int,input(' ').strip().split()))[:n]
  k = int(input())
  b = list(map(int,input(' ').strip().split()))[:k]
  
  ans = set(a) - set(b)
  res = []
  for i in a:
    if i in ans:
      res.append(i)
  print(' '.join(map(str, res)))