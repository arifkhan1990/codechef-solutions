for _ in range(int(input())):
    n = int(input())
    direction = []
    place = []
    for i in range(n):
        s = input()
        place.append(s)
    for i in place[::-1]:
        if direction == []:
            direction.append(i.replace('Right','Begin') if i[0] == 'R' else i.replace('Left','Begin'))
        else:
            if i[0] == 'R':
                direction.append(i.replace('Right', direc))
            elif i[0] == 'L':
                direction.append(i.replace('Left', direc))
            else:
                direction.append(i.replace('Begin', direc))
        direc = 'Left' if i[0] == 'R' else 'Right'
    print(*direction, sep='\n')