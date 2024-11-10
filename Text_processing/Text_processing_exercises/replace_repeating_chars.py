text = input()
current_char = ""
new_text = ""
for char in text:
    if char != current_char:
        new_text += char
        current_char = char

print(new_text)