import re

text = input()

all_numbers = r"\d"
regex = r"\*\*[A-Z][a-z]{2,}\*\*|\:\:[A-Z][a-z]{2,}\:\:"

matches = re.findall(regex, text)
nums = re.findall(all_numbers, text)

cool_threshold = 1
for num in nums:
    cool_threshold *= int(num)

print(f"Cool threshold: {cool_threshold}")
print(f"{len(matches)} emojis found in the text. The cool ones are:")

for match in matches:
    cool_points = 0
    new_match = match[2:-2]
    for char in new_match:
        cool_points += ord(char)
    if cool_points >= cool_threshold:
        print(match)