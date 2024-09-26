number = input()

for digit in number:
    digits = list(number)
    digits_sorted = sorted(digits, reverse=True)
    largest_number = "".join(digits_sorted)
print(largest_number)
