message = input()
code = ""

for char in message:
    current = ord(char) + 3
    code += chr(current)

print(code)