def drive(owned_cars, commands):
    distance = int(commands[2])
    fuel_needed = int(commands[3])
    if fuel_needed > owned_cars[car]["fuel"]:
        print("Not enough fuel to make that ride")
    else:
        owned_cars[car]["mileage"] += distance
        owned_cars[car]["fuel"] -= fuel_needed
        print(f"{car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")
        if owned_cars[car]["mileage"] >= 100000:
            print(f"Time to sell the {car}!")
            del owned_cars[car]
    return owned_cars


def refuel(owned_cars, commands):
    fill_fuel = int(commands[2])
    if owned_cars[car]["fuel"] + fill_fuel > 75:
        print(f"{car} refueled with {75 - owned_cars[car]['fuel']} liters")
        owned_cars[car]["fuel"] = 75
    else:
        cars[car]["fuel"] += fill_fuel
        print(f"{car} refueled with {fill_fuel} liters")
    return owned_cars


def revert(owned_cars, commands):
    kilometers = int(commands[2])
    owned_cars[car]["mileage"] -= kilometers
    if owned_cars[car]["mileage"] < 10000:
        owned_cars[car]["mileage"] = 10000
    else:
        print(f"{car} mileage decreased by {kilometers} kilometers")
    return owned_cars

number_of_cars = int(input())
cars = {}

for _ in range(number_of_cars):
    model, mileage, fuel = input().split("|")
    mileage = int(mileage)
    fuel = int(fuel)
    cars[model] = {}
    cars[model]["mileage"] = mileage
    cars[model]["fuel"] = fuel

while True:
    command = input()
    if command == "Stop":
        break
    parts = command.split(" : ")
    action = parts[0]
    car = parts[1]
    if action == "Drive":
        cars = drive(cars, parts)
    elif action == "Refuel":
        cars = refuel(cars, parts)
    elif action == "Revert":
        cars = revert(cars, parts)

for car, info in cars.items():
    mileage = info["mileage"]
    fuel = info["fuel"]
    print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")
