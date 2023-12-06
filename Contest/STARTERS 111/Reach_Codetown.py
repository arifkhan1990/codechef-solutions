for _ in range(int(input())):
  s = input()
  if (s[1] in "AEIOU" and s[3] in "AEIOU" and s[5] in "AEIOU"):
    if s[0] not in "AEIOU" and s[2] not in "AEIOU" and s[4] not in "AEIOU" and s[6] not in "AEIOU" and s[7] not in "AEIOU":
      print("YES")
    else:
      print("NO")
  else:
    print("NO")