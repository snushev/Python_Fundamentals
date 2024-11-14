# import re
#
# regex = r">>(?P<product>[A-Za-z]+)<<(?P<price>[0-9]+([.0-9]+)?)!(?P<quantity>\d+)"
# total = 0
# products = []
# while True:
#     line = input()
#     if line == "Purchase":
#         break
#
#     matches = re.finditer(regex, line)
#     if not matches:
#         continue
#     for match in matches:
#         product_name = match.group('product')
#         price_value = float(match.group('price'))
#         quantity_value = int(match.group('quantity'))
#         total += price_value * quantity_value
#         products.append(product_name)
# print("Bought furniture:")
# for product in products:
#     print(product)
# print(f"Total money spend: {total:.2f}")

import re

regex = r">>([A-Za-z]+)<<([0-9]+[.0-9]+?)!(\d+)"
total = 0
products = []
while True:
    line = input()
    if line == "Purchase":
        break

    matches = re.findall(regex, line)
    if not matches:
        continue
    for match in matches:
        product_name = match[0]
        price_value = float(match[1])
        quantity_value = int(match[2])
        total += price_value * quantity_value
        products.append(product_name)
print("Bought furniture:")
for product in products:
    print(product)
print(f"Total money spend: {total:.2f}")