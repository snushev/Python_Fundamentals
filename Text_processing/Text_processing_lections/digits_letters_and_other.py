text = input()
digits = ""
letter = ""
other = ""

for char in text:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letter += char
    else:
        other += char

print(f"{digits}\n{letter}\n{other}")