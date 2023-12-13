def net_amount(n, k):
    amount_paid = n - (n//(k+1))*(k)
    return amount_paid

# Example usage:
for _ in range(int(input())):
    n, k = map(int, input().split())
    result = net_amount(n, k)
    print(result)

