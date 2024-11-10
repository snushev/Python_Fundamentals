text = input().split()
total = 0
for current_text in text:
    first_letter_num = ord(current_text[0].lower()) - ord('a') + 1
    last_letter_num = ord(current_text[-1].lower()) - ord('a') + 1
    current_num = int(current_text[1:-1])
    if current_text[0].isupper():
        current_num /= first_letter_num
    elif current_text[0].islower():
        current_num *= first_letter_num
    if current_text[-1].isupper():
        current_num -= last_letter_num
    elif current_text[-1].islower():
        current_num += last_letter_num
    total += current_num
print(f"{total:.2f}")

