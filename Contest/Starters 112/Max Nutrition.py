def max_nutrition_value(n, types, nutrition_values):
    # Combine types and nutrition values into a list of tuples
    fruits = list(zip(types, nutrition_values))

    # Sort the fruits based on nutrition values in descending order
    sorted_fruits = sorted(fruits, key=lambda x: x[1], reverse=True)

    eaten_types = set()
    max_nutrition = 0

    for fruit in sorted_fruits:
        fruit_type, nutrition = fruit
        if fruit_type not in eaten_types and nutrition > 0:
            max_nutrition += nutrition
            eaten_types.add(fruit_type)

    return max_nutrition


for _ in range(int(input())):
    n = int(input())
    types = list(map(int, input().split()))
    nutrition_values = list(map(int, input().split()))

    result = max_nutrition_value(n, types, nutrition_values)
    print(result)
