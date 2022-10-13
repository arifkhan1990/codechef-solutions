from sys import stdin
ip = stdin.readline

for _ in range(int(ip())):
    s = ip()
    s = s.lower()
    letter = {}
    for i in 'abcdefghijklmnopqrstuvwxyz':
        letter[i] = 1 if i in s else 0
    
    ans =  min(letter, key=letter.get)
    print('~' if letter[ans] == 1 else ans)