number_of_cities = int(input())
total_profit = 0

for city in range(1, number_of_cities + 1):
    name_of_the_city = input()
    owners_income = float(input())
    owners_expense = float(input())
    if city % 3 == 0 and city % 5 != 0:
        owners_expense *= 1.5
    if city % 5 == 0:
        owners_income *= 0.9
    current_profit = owners_income - owners_expense
    total_profit += current_profit

    print(f"In {name_of_the_city} Burger Bus earned {current_profit:.2f} leva.")
print(f"Burger Bus total profit: {total_profit:.2f} leva.")