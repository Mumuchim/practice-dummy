numbers = ["C", "A", "B"]
highest_value_in_array = numbers[0]
for number in numbers:
    if number > highest_value_in_array:
        highest_value_in_array = number
print(highest_value_in_array)
