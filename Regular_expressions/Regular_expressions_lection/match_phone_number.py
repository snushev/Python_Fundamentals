import re

pattern = input()
regex = r"\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4}\b"
matches = re.findall(regex, pattern)

print(*matches, sep=', ')