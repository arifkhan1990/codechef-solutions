for _ in range(int(input())):
  x , y = map(int, input().split())
  if (x%2 and y%2) or (x == 1 or y == 1):
    print(-1)
  else:
    a = 'a'*x
    b = 'b'*y
    if x%2:
      s1 = b[:y//2] + a + b[y//2:]
      s2 = a[:x//2] + b[:y//2] + 'a' + b[y//2:] + a[(x//2)+1:]
    elif y%2:
      s1 = a[:x//2] + b + a[x//2:]
      s2 = b[:y//2] + a[:x//2] + 'b' + a[x//2:] + b[(y//2)+1:]
    else:
      s1 = b[:y//2] + a + b[y//2:]
      s2 = a[:x//2] + b + a[x//2:]

    print(s1)
    print(s2)