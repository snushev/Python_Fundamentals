data = input()
products = {}
while data != "statistics":
    key, value = data.split(": ")
    value = int(value)
    if key not in products:
        products[key] = value
    else:
        products[key] += value

    data = input()
print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
print(f'Total Products: {len(products.keys())}')
print(f'Total Quantity: {sum(products.values())}')