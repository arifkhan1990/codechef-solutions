for _ in range(int(input())):
    s, a,b, c = map(int, input().split())

    bS = s + (s * (c/100))
    print('Yes' if bS >= a and bS <= b else 'No')