import re

text = input()
regex = r"([\=\/])([A-Z][A-Za-z]{2,})\1"
matches = re.findall(regex, text)
destinations = []
points = 0
for match in matches:
    destinations.append(match[1])
    points += len(match[1])

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {points}")