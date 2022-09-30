for _ in range(int(input())):
    n = int(input())
    s = input()
    count_1 = s.count('1')
    print((count_1*(count_1+1))//2)