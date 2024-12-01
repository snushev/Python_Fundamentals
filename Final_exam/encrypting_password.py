import re

n = int(input())

for i in range(n):
    password = input()

    regex = r"(.+?)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^\<>\s]{3})<\1"

    matches = re.finditer(regex, password)

    another_pass = True

    for match in matches:
        pas = match.group(2) + match.group(3) + match.group(4) + match.group(5)
        print(f"Password: {pas}")

        another_pass = False

    if another_pass:
        print("Try another password!")