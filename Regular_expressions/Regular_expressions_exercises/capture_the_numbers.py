import re

lst = []

while True:
    text = input().strip()

    if text == "":
        break
    regex = r"\d+"
    matches = re.findall(regex, text)
    lst.extend(matches)

print(*lst)
