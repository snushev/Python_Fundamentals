command = input()
items = {}
while command != "buy":
    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)
    if name not in items:
        items[name] = [price, quantity]
    else:
        items[name][0] = price
        items[name][1] += quantity
    command = input()

for item, values in items.items():
    price, quantity = values
    total = price * quantity
    print(f"{item} -> {total:.2f}")
