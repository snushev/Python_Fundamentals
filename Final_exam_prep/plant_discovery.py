n = int(input())
plants = {}

for i in range(n):
    plant_info = input().split('<->')
    plant_name = plant_info[0]
    plant_rarity = plant_info[1]
    plants[plant_name] = {}
    plants[plant_name]['rarity'] = plant_rarity
    plants[plant_name]['rating'] = []

while True:
    command = input()
    if command == "Exhibition":
        break

    parts = command.split(': ')
    action = parts[0]
    if action == "Rate":
        plant, rating = parts[1].split(' - ')
        rating = int(rating)
        if plant in plants:
            plants[plant]['rating'].append(rating)
        else:
            print('error')
    elif action == "Update":
        plant, new_rarity = parts[1].split(' - ')
        if plant in plants:
            plants[plant]['rarity'] = new_rarity
        else:
            print('error')
    elif action == "Reset":
        plant = parts[1]
        if plant in plants:
            plants[plant]['rating'] = []
        else:
            print('error')

print("Plants for the exhibition:")
for plant, info in plants.items():
    if len(info['rating']) > 0:
        average_rating = sum(info['rating']) / len(info['rating'])
        print(f"- {plant}; Rarity: {info['rarity']}; Rating: {average_rating:.2f}")
    else:
        print(f"- {plant}; Rarity: {info['rarity']}; Rating: 0.00")
