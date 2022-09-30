from math import gcd
from functools import reduce
for _ in range(int(input())):
	n, k = map(int, input().split())
	a = list(map(int, input().split()))
	G = reduce(gcd, a)
	cur = taken = 0
	for i in range(n):
		cur = gcd(cur, a[i])
		if cur == G:
			cur = 0
			taken += 1
	print('Yes' if taken >= k else 'No')
