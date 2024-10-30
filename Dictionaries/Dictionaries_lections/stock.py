products = {}
data = input().split()

for index in range(0, len(data), 2):
    key = data[index]
    value = int(data[index + 1])
    products[key] = value

wanted_products = input().split()

for item in wanted_products:
    if item in products:
        print(f"We have {products[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")