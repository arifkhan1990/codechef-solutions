from sys import stdin
ip = stdin.readline
from collections import Counter
for _ in range(int(ip())):
    n = int(ip())
    card = list(map(int,ip().split()))
    cardDic = Counter(card)
    top = cardDic.most_common(1)
    print(len(card) - top[0][1])

