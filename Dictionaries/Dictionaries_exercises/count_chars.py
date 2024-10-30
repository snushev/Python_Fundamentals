text = input()
chars = {}

for char in text:
    if char != ' ':
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

for item in chars:
    print(f"{item} -> {chars[item]}")