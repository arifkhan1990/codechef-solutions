def find_ABC(N):
    A = 1
    while True:
        if N & 1:
            break
        N //= 2
        A *= 2
    
    if N == 1:
        return [-1]
    else:
        N = N // 2
        return N*A, A, A


T = int(input())
for _ in range(T):
    N = int(input())
    result = find_ABC(N)
    print(*result)




#         # cook your dish here


# hErd gives you an integer N. Find any three positive integers A,B,C such that:
# N=lcm(A,B)+lcm(B,C)+lcm(C,A); where lcm denotes the least common multiple.
# If there is no solution, print −1.
# If there are multiple solutions, you may print any of them.

# Input:
# 3
# 1
# 6
# 15

# Output:
#   -1
# 2 2 2
# 5 5 1

# Explanation:
# Test case 
# 1: It can be shown that no solution exists.

# Test case 2: Consider A=2,B=2,C=2. Thus, 6=lcm(2,2)+lcm(2,2)+lcm(2,2).

# Test case 3: Consider A=5,B=5,C=1. Thus, 15=lcm(5,5)+lcm(5,1)+lcm(5,1).
# Note that 
# (5,5,1),(1,5,5) and (5,1,5) are all considered valid.
