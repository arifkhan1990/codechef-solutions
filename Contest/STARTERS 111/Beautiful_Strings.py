MOD = 10**9 + 7

def calculate_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def count_beautiful_strings(n, s):
    s_frequency = calculate_frequency(s)
    result = 1

    for count in s_frequency.values():
        result = (result * (count + 1)) % MOD

    return result - 1  # Subtract 1 to exclude the empty string

# Input reading
t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    result = count_beautiful_strings(n, s)
    print(result)
