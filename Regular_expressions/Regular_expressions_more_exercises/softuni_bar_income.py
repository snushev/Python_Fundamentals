import re

regex = r"%(?P<Name>[A-Z][a-z]*)%.*?<(?P<Product>[A-Z][a-z]*)>.*?\|(?P<Quantity>\d+)\|.*?(?P<Price>\d+(?:\.\d+)?)\$"

total = 0

while True:
    line = input()
    if line == "end of shift":
        break

    matches = re.match(regex, line)
    if not matches:
        continue

    name = matches.group("Name")
    product = matches.group("Product")
    quantity = int(matches.group("Quantity"))
    price = float(matches.group("Price"))
    print(f"{name}: {product} - {quantity * price:.2f}")
    total += price * quantity

print(f"Total income: {total:.2f}")
