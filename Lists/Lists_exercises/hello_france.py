collect_of_items = input().split('|')
budget = float(input())
ticket_price = 150
money_for_shopping = 0
money_from_selling = 0
selling_price_list = []

for item in collect_of_items:
    current_item = item.split('->')
    item_type = current_item[0]
    current_item_price = float(current_item[1])
    if budget < current_item_price:
        continue
    if item_type == 'Clothes' and current_item_price <= 50:
        budget -= current_item_price
        selling_price = current_item_price * 1.4
        money_for_shopping += current_item_price
        money_from_selling += selling_price
        selling_price_list.append(f'{selling_price:.2f}')
    elif item_type == 'Shoes' and current_item_price <= 35:
        budget -= current_item_price
        selling_price = current_item_price * 1.4
        money_for_shopping += current_item_price
        money_from_selling += selling_price
        selling_price_list.append(f'{selling_price:.2f}')
    elif item_type == 'Accessories' and current_item_price <= 20.50:
        budget -= current_item_price
        selling_price = current_item_price * 1.4
        money_for_shopping += current_item_price
        money_from_selling += selling_price
        selling_price_list.append(f'{selling_price:.2f}')

print(" ".join(selling_price_list))
profit = money_from_selling - money_for_shopping
print(f'Profit: {profit:.2f}')
budget += money_from_selling
if budget >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")