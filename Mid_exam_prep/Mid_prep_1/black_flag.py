

days_in_sea = int(input())
daily_plunder = int(input())
expected_plunder = float(input())

total_plunder = 0
for days_in_sea in range(1, days_in_sea + 1):
    total_plunder += daily_plunder
    if days_in_sea % 3 == 0:
        total_plunder += 0.5 * daily_plunder
    if days_in_sea % 5 == 0:
        total_plunder -= 0.3 * total_plunder

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    percentage = (total_plunder / expected_plunder) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")
