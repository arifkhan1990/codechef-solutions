from collections import Counter
import math
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int,input(' ').strip().split()))[:n]
    dis_n = Counter(nums).most_common(1)
    
    mx = 0
    for key, value in dis_n:
        mx = value
    
    print(0 if mx == 0 else math.ceil(math.log2(mx)))