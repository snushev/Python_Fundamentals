lost_fight_count = int(input())

helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_repairs = 0
sword_repairs = 0
shield_repairs = 0
armor_repairs = 0

for fight in range(1, lost_fight_count + 1):
    if fight % 2 == 0:
        helmet_repairs += 1
    if fight % 3 == 0:
        sword_repairs += 1
    if fight % 2 == 0 and fight % 3 == 0:
        shield_repairs += 1
    if fight % 12 == 0:
        armor_repairs += 1

total_cost = (helmet_price * helmet_repairs) + (sword_price * sword_repairs) + (shield_price * shield_repairs) + (
            armor_price * armor_repairs)

print(f"Gladiator expenses: {total_cost:.2f} aureus")
