# cook your dish here
T = int(input())
for i in range(T):
  x, y = map(int, input().split(' '))
  z = (x*3)
  x =  z - (y+y)
  print(x , y , y, end = ' ')
  print()
