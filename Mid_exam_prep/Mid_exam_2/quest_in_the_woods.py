days = int(input())
people = int(input())
group_energy = float(input())
water_for_one_per_day = float(input())
food_for_one_per_day = float(input())

total_water = water_for_one_per_day * days * people
total_food = food_for_one_per_day * days * people

for day in range(1, days + 1):
    energy_loss = float(input())
    group_energy -= energy_loss

    if group_energy <= 0:
        print(f"You will run out of energy. You will be left with {total_food} food and {total_water} water.")
        break