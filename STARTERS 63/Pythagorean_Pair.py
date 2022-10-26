# From math import everything
from math import *

def countPairs(N) :
    ans = []
    for i in range(1, int(sqrt(N)) + 1) :
        sq = i * i
 
        diff = N - sq

        sqrtDiff = int(sqrt(diff))

        if sq  +  (sqrtDiff*sqrtDiff) == N :
            ans = [i, sqrtDiff]
            break
    return ans

for _ in range(int(input())):
    n = int(input())
    ans = countPairs(n)
    if ans == []:
        print(-1)
    else:
        print(*ans)