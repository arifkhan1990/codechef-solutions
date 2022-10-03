n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = sorted([(-y,x) for x,y in zip(a,b)])
for i in ans:
  print(i[1],-i[0], end=' ')