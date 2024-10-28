money_per_search = float(input())
number_of_users = int(input())
total_money = 0
a = money_per_search
for user in range(1, number_of_users + 1):
    number_of_searches = int(input())
    if number_of_searches > 1:
        if user % 3 == 0:
            a *= 3
        if number_of_searches > 5:
            a *= 2
        total_money += a * number_of_searches
    a = money_per_search

print(f"Total money earned: {total_money:.2f}")