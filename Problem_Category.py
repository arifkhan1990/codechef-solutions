for _ in range(int(input())):
    n = int(input())
    if n > 0 and n < 100:
        print('Easy')
    elif n >= 100 and n < 200:
         print('Medium')
    else:
        print('Hard')