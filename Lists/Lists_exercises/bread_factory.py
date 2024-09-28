energy = 100
coins = 100
working_day_events = input().split("|")
bakery_is_open = True

for event in working_day_events:
    current_event = event.split('-')
    event_type = current_event[0]
    event_value = int(current_event[1])
    # if energy < 30:
    #     print("You had to rest!")
    #     energy += 50
    if event_type == "rest":
        energy += event_value
        if energy >= 100:
            print(f'You gained 0 energy.')
            print(f'Current energy: 100.')
            energy = 100
        else:
            print(f'You gained {event_value} energy.')
            print(f'Current energy: {energy}.')
    elif event_type == "order":
        if energy < 30:
            print("You had to rest!")
            energy += 50
        else:
            print(f'You earned {event_value} coins.')
            coins += event_value
            energy -= 30
    else:
        if coins <= event_value:
            print(f"Closed! Cannot afford {event_type}.")
            bakery_is_open = False
            break
        else:
            print(f"You bought {event_type}.")
            coins -= event_value

if bakery_is_open:
    print(f'Day completed!\nCoins: {coins}\nEnergy: {energy}')
