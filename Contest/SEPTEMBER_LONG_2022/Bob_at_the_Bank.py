T = int(input())
for i in range(T):
    w, x, y, z = map(int, input().split())
    print(w + (x-y)*z)