for _ in range(int(input())):
  n = int(input())
  ar = list(map(int, input().split()))
  sm = [1]*n
  for i in range(1,n):
    if ar[i] >= ar[i-1]:
      sm[i] = sm[i-1] + 1

  print(sum(sm))