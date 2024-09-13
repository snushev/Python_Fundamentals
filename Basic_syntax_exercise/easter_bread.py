budget = float(input())
flour_price = float(input())
egg_price = flour_price * 0.75
milk_price = (flour_price * 1.25) / 4

price = flour_price + egg_price + milk_price

colored_eggs = 0
loafs = 0

while budget > price:
    loafs += 1
    colored_eggs += 3
    if loafs % 3 == 0:
        colored_eggs -= (loafs - 2)
    budget -= price
money_left = abs(budget)
print(f'You made {loafs} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.')
