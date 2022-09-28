for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input(' ').strip().split()))[:n]

    ans = 0
    od = ev = 0

    for i in nums:
        if i%2 == 0:
            od += 1

    if (od == n):
        print(0)
    else:
        print(od)
        