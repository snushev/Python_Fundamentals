sequence = input().split()

new_string = ""

for word in sequence:
    new_string += word * len(word)

print(new_string)