exp_needed = int(input())
count_of_battles = int(input())

for current_battle in range(1, count_of_battles + 1):
    exp_gained = int(input())
    if current_battle % 3 == 0:
        exp_gained *= 1.15
    if current_battle % 5 == 0:
        exp_gained *= 0.9
    if current_battle % 15 == 0:
        exp_gained *= 1.05
    exp_needed -= exp_gained
    if exp_needed <= 0:
        print(f"Player successfully collected his needed experience for {current_battle} battles.")
        break

else:
    print(f"Player was not able to collect the needed experience, {exp_needed:.2f} more needed.")