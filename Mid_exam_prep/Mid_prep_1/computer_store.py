part_price = input()

total_price_without_taxes = 0
total_amount_of_taxes = 0
total_price_with_taxes = 0

while True:

    if part_price == "special":
        if total_price_with_taxes > 0:
            total_price_with_taxes *= 0.9
        break
    elif part_price == "regular":
        break
    elif float(part_price) < 0:
        print("Invalid price!")
    else:
        price_without_tax = float(part_price)
        price_with_tax = price_without_tax * 1.20
        total_price_without_taxes += price_without_tax
        total_amount_of_taxes += price_with_tax - price_without_tax
        total_price_with_taxes += price_with_tax
    part_price = input()

if total_price_without_taxes != 0:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_without_taxes:.2f}$")
    print(f"Taxes: {total_amount_of_taxes:.2f}$")
    print(f"-----------")
    print(f"Total price: {total_price_with_taxes:.2f}$")
else:
    print("Invalid order!")