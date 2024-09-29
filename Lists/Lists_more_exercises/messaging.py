numbers = input().split()
text = input()
new_text = ""

for number in numbers:
    current_sum_of_digits = 0
    for digit in number:
        current_sum_of_digits += int(digit)
    char = text[current_sum_of_digits % len(text)]
    new_text += char
    text = text[:current_sum_of_digits % len(text)] + text[(current_sum_of_digits % len(text)) + 1:]

print(new_text)
