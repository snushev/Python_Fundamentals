from math import floor

biscuits_per_person_per_day = int(input())
workers = int(input())
biscuits_of_enemy = int(input())
bad_day = 0
total_biscuits_per_day = workers * biscuits_per_person_per_day
for day in range(1, 31):
    if day % 3 == 0:
        bad_day += floor(total_biscuits_per_day * 0.25)
total_biscuits = 30 * total_biscuits_per_day - bad_day

print(f"You have produced {total_biscuits} biscuits for the past month.")

if total_biscuits > biscuits_of_enemy:
    diff = total_biscuits - biscuits_of_enemy
    percent = diff / biscuits_of_enemy * 100
    print(f"You produce {percent:.2f} percent more biscuits.")
elif biscuits_of_enemy > total_biscuits:
    diff = biscuits_of_enemy - total_biscuits
    percent = diff / total_biscuits * 100
    print(f"You produce {percent:.2f} percent less biscuits.")

