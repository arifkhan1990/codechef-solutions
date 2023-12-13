def solve(N, preferences):

    responses = []
    b = 0
    for i in range(N-1):
        if b or preferences[i] == '0':
            responses.append("NO")
            b = 1
        else:
            responses.append("IDK")
    if b == 0 and preferences[-1] == '1':
        responses.append("YES")
    else:
        responses.append("NO")
    return responses


for _ in range(int(input())):
    N = int(input())
    S = input()
    result = solve(N, S)
    for i in result:
        print(i)
