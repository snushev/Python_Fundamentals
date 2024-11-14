import re

text = input()
regex = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
matches = re.finditer(regex, text)

for match in matches:
    lst = match.group()
    print(lst, end=" ")
