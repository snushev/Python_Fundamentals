numbers = input().split(', ')
modified_numbers = []
zero_numbers = []
for number in numbers:
    if int(number) != 0:
        modified_numbers.append(int(number))
    else:
        zero_numbers.append(int(number))
modified_numbers.extend(zero_numbers)
print(modified_numbers)