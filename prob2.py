strings = ["red", "blue", "orange", "green", "purple"]

sorted_strings = sorted(strings, key=lambda x: (len(x), x))
print(sorted_strings)