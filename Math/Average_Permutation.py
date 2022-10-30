# cook your dish here
for _ in range(int(input())):
  n = int(input())
  for i in range(n,0,-1):
      if i&1 == 0:
          print(i,end=" ")
  for i in range(1,n+1):
      if i&1 != 0:
          print(i,end=' ')
  print()