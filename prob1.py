number = 12345

sum_of_digits = lambda x: sum(int(digit) for digit in str(x) if digit.isdigit())

result = sum_of_digits(number)
print("Sum of digits of", number, "is:", result)