def find_maximum(numbers, comparison_function):
    maximum = numbers[0]
    for num in numbers[1:]:
        maximum = comparison_function(maximum, num)
    return maximum


numbers = [5, 10, 35, 20, 25]
max_number = find_maximum(numbers, lambda x, y: x if x > y else y)
print(max_number)