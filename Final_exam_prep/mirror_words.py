import re

text = input()
regex = r"([#@])([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1"
matches = re.findall(regex, text)
words = {}

for match in matches:
    if match[1] == match[2][::-1]:
        words[match[1]] = match[2]

if len(matches) > 0:
    print(f"{len(matches)} word pairs found!")
else:
    print("No word pairs found!")

if words:
    print("The mirror words are:")
    for index, (word, reverse) in enumerate(words.items()):
        if index < len(words) - 1:
            print(f"{word} <=> {reverse}", end=', ')
        else:
            print(f"{word} <=> {reverse}")
else:
    print("No mirror words!")