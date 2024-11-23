import re
total_calories = 0
items = []

text = input()
regex = r'([#|])(?P<item>[a-zA-Z\s]+)\1(?P<exp_date>\d{2}\/\d{2}\/\d{2})\1(?P<cal>\d{1,5})\1'
matches = re.finditer(regex, text)
for match in matches:
    item = match['item']
    exp_date = match['exp_date']
    cal = int(match['cal'])
    total_calories += cal
    items.append(f"Item: {item}, Best before: {exp_date}, Nutrition: {cal}")

days = total_calories // 2000
print(f"You have food to last you for: {days} days!")

for i in items:
    print(i)

