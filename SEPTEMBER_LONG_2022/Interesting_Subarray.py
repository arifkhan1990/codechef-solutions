T = int(input())
for i in range(T):
    n = int(input())
    arr = list(map(int,input(' ').strip().split()))[:n]

    minimam = min(arr)
    maximum = max(arr)

    ProArrN = [x * minimam for x in arr]
    ProArrM = [x * maximum for x in arr]

    Pro = ProArrN + ProArrM
    Pro.sort()

    print(Pro[0], Pro[-1], sep=' ')