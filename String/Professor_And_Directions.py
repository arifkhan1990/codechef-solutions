# cook your dish here
for _ in range(int(input())):
  n = int(input())
  s = input()
  if s.find('LL') != -1 or s.find('RR') != -1:
    print('YES')
  else:
    print('NO')