T = int(input())
for i in range(T):
    n = int(input())

    g = list(map(int,input(' ').strip().split()))[:n]
    w = list(map(int,input(' ').strip().split()))[:n]
    
    g1 = dict(zip(range(len(g)), g))
    w1 = dict(zip(range(len(w)), w))

    g1 = dict(sorted(g1.items(), key=lambda item: item[1]))
    w1 = dict(sorted(w1.items(), key=lambda item: item[1]))

    ans = [0]*n
    gS = wS = []

    gS = list(g1.keys())
    wS = list(w1.keys())

    for i in range(n-1, -1, -1):
        ans[wS[i]] += i
        wl = gS.index(wS[i])
        ans[wS[i]] += len(gS[:wl]) - (len(set(gS[0:wl]) - set(wS[i:])))

        # ans[gS[i]] += i
        # wl = wS.index(gS[i])
        # ans[gS[i]] +=   len(wS[0:wl]) - (len(set(wS[0:wl]) - set(gS[i:])))
        # print(ans)

    maximum = max(ans)
    qualify = ans.count(maximum)
    print(qualify)