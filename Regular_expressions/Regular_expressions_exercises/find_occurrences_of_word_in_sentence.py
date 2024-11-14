import re

text = input()
word = input()

regex = r"\b" + re.escape(word) + r"\b"

matches = re.findall(regex, text, re.IGNORECASE)

print(len(matches))