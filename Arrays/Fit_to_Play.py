for _ in range(int(input())):
  n = int(input())
  ar = list(map(int, input().split( )))
  ans = 0
  res = ar[0]
  for i in range(1,n):
    res = min(res,ar[i])
    ans = max(ans, ar[i] - res)
  print('UNFIT' if ans == 0 else ans)