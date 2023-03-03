m = [0]*100001
isP = [1]*100001
i =  2
while i*i <= 100001:
    if isP[i] == 1:
        j = i+i
        while j < 100001:
            isP[j] = 0
            j += i
    i += 1
        
for i in range(2, 100001):
    if isP[i] == 1:
        j = i
        while j < 100001:
            m[j] += 1
            j += i

for _ in range(int(input())):
    a, b, k = map(int,input().split())
    ans = 0
    for i in range(a, b+1):
        # print(i, m[i])
        if m[i] == k:
            ans += 1
    print(ans)