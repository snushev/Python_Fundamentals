def order(product: str, quantity: int):
    if product == 'coffee':
        return quantity * 1.5
    elif product == 'coke':
        return quantity * 1.4
    elif product == 'water':
        return quantity
    elif product == 'snacks':
        return quantity * 2


product = input()
quantity = int(input())

total_price = order(product, quantity)
print(f'{total_price:.2f}')