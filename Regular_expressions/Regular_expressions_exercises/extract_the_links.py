import re

regex = r"www\.[A-Za-z0-9-]+(\.[a-z]+)+"

while True:
    line = input()
    if line == "":
        break

    matches = re.search(regex, line)

    if matches:
        print(matches[0])