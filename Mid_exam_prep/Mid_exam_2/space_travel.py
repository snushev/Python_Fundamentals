travel_route = input().split('||')
fuel = int(input())
ammo = int(input())

for step in travel_route:
    data = step.split(" ")
    command = data[0]

    if len(data) < 2:  # Added command format validation
        print("Invalid command format.")
        continue

    value = int(data[1])

    if command == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break

    if command == "Travel":
        if fuel >= value:  # Adjusted fuel check
            fuel -= value
            print(f"The spaceship travelled {value} light-years.")
        else:
            print("Mission failed.")
            break

    elif command == "Enemy":
        if ammo >= value:
            ammo -= value
            print(f"An enemy with {value} armour is defeated.")
        else:
            if fuel >= value * 2:  # Adjusted fuel check for running away
                fuel -= value * 2
                print(f"An enemy with {value} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break

    elif command == "Repair":
        fuel += value
        ammo += value * 2
        print(f"Ammunitions added: {value * 2}.")
        print(f"Fuel added: {value}.")
