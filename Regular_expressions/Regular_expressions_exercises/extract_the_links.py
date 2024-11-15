import re

regex = r"www\.[a-z0-9-]+(\.[a-z]+)+"

while True:
    line = input()
    if line == "":
        break

    matches = re.finditer(regex, line)

    for match in matches:
        print(match.group(0))