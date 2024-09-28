fire_list = input().split('#')
water = int(input())
effort = 0
total_fire = 0
print("Cells:")

for fire in fire_list:
    fire_parts = fire.split(' = ')
    fire_type = fire_parts[0]
    fire_power = int(fire_parts[1])
    if (fire_type == 'High' and 81 <= int(fire_power) <= 125) or \
            (fire_type == 'Medium' and 51 <= int(fire_power) <= 80) or \
            (fire_type == 'Low' and 1 <= int(fire_power) <= 50):
        if water >= fire_power:
            print(f' - {fire_power}')
            effort += fire_power * 0.25
            total_fire += fire_power
            water -= fire_power
        else:
            continue
    else:
        continue

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
