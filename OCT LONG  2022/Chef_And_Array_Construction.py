from sys import stdin
ip = stdin.readline

def permutation(n, arr, Len, L):

    ar = []
    sm = 0
    for i in range(L):
        sm = arr[n % Len] if i == 0 else sm
        ar.append(arr[n % Len])
        sm = sm & arr[n % Len]
        n //= Len
    return sm%998244353
 
def printf(arr, Len, L):
    ar = 0
    for i in range(pow(Len, L)):
        ar += permutation(i, arr, Len, L)
    return ar%998244353
            
for _ in range(int(ip())):
    n, m = map(int, ip().split())
    li = [i for i in range(1,m+1)]
    print(printf(li, m, n))