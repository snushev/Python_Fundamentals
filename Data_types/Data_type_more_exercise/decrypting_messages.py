key = int(input())
number_of_lines = int(input())

password = ""

for _ in range(number_of_lines):
    line = input()
    current_char = ord(line) + key
    password += chr(current_char)
print(password)