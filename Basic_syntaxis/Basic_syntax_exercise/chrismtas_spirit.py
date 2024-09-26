quantity = int(input())
days = int(input())
money_spent = 0
christmas_spirit = 0
ornament_set = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15
for i in range(1, days + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        money_spent += quantity * ornament_set
        christmas_spirit += 5
    if i % 3 == 0:
        money_spent += (tree_skirt + tree_garland) * quantity
        christmas_spirit += 13
    if i % 5 == 0:
        money_spent += tree_lights * quantity
        christmas_spirit += 17
    if i % 10 == 0:
        money_spent += tree_skirt + tree_garland + tree_lights
        christmas_spirit -= 20
    if i % 15 == 0:
        christmas_spirit += 30
if days % 10 == 0:
    christmas_spirit -= 30
print(f'Total cost: {money_spent}')
print(f'Total spirit: {christmas_spirit}')

counter = 0
