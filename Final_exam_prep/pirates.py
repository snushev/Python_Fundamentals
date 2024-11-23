targets = {}

while True:
    command = input()

    if command == "Sail":
        break

    parts = command.split('||')
    city = parts[0]
    population = int(parts[1])
    gold = int(parts[2])
    if city not in targets:
        targets[city] = {'population': 0, 'gold': 0}
    targets[city]['population'] += population
    targets[city]['gold'] += gold

while True:
    command = input()
    if command == "End":
        break

    parts = command.split('=>')
    action = parts[0]
    city = parts[1]

    if action == "Plunder":
        people = int(parts[2])
        gold = int(parts[3])
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        targets[city]['population'] -= people
        targets[city]['gold'] -= gold
        if targets[city]['population'] <= 0 or targets[city]['gold'] <= 0:
            del targets[city]
            print(f"{city} has been wiped off the map!")

    elif action == "Prosper":
        gold = int(parts[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            targets[city]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {targets[city]['gold']} gold.")


if targets:
    print(f"Ahoy, Captain! There are {len(targets)} wealthy settlements to go to:")
    for city, data in targets.items():
        print(f"{city} -> Population: {data['population']} citizens, Gold: {data['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")

