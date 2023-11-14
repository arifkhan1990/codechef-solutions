for _ in range(int(input())):
    n = int(input())
    s = input()
    l1,l2,r1,r2  = '0', '0' , '0', '0'
    for i in range(n):
        if s[i] == '1':
            if r1 == '0':
                r1 = i
            else:
                r2 = i
        else:
            if l1 == '0':
                l1 = i
            else:
                l2 = i
    
    if l1 != l2 != '0':
        n2 = s[l1:l2+1]
    elif l1 != '0' and l2 == '0':
        n2 = s[l1:l1+1]
    else:
        n2 = ''
    if r1 != r2 != '0':
        n1 = s[r1:r2+1]
    elif r1 != '0' and r2 == '0':
        n1 = s[r1:r1+1]
    else:
        n1 = ''
    print(l1,l2,r1,r2,n1,n2)
    n1 = 0 if n1 == '' else int(n1,2)
    n2 =  0 if n2 == '' else int(n2,2)
    print(n1,n2, n1^n2)