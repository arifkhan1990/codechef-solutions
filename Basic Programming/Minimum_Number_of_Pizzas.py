from sys import stdin
import math
i_p = stdin.readline
for _ in range(int(i_p())):
    p,k = map(int, i_p().split())
    print(p//math.gcd(p,k))