from collections import Counter
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input(' ').strip().split()))[:n]
    mx = Counter(nums).most_common(1)
    for key, value in mx:
        print(n - value)
        break