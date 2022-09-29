for _ in range(int(input())):
    n ,a ,b,c = map(int, input().split())
    
    dish = (a+c) if (a+c) < b else b
    print("YES" if dish >= n else "NO")

