stocks = {}
sold_stocks = 0

while True:
    command = input()
    if command == 'Complete':
        break

    parts = command.split()
    action = parts[0]
    quantity = int(parts[1])
    food = parts[2]

    if action == "Receive" and quantity > 0:
        if food not in stocks:
            stocks[food] = 0
        stocks[food] += quantity
    elif action == "Sell":
        if food not in stocks:
            print(f"You do not have any {food}.")
        elif food in stocks and quantity <= stocks[food]:
            stocks[food] -= quantity
            sold_stocks += quantity
            if stocks[food] == 0:
                del stocks[food]
            print(f"You sold {quantity} {food}.")
        elif food in stocks and quantity > stocks[food]:
            print(f"There aren't enough {food}. You sold the last {stocks[food]} of them.")
            sold_stocks += stocks[food]
            stocks[food] = 0
            del stocks[food]


for food, quantity in stocks.items():
    print(f"{food}: {quantity}")
print(f"All sold: {sold_stocks} goods")