rooms = input().split('|')

health = 100
bitcoins = 0
best_room = 0
is_dead = False

for room in rooms:
    best_room += 1
    command, number = room.split(' ')
    if command == 'potion':
        initial_health = health
        health += int(number)
        if health > 100:
            health = 100
        amount = health - initial_health
        print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")

    elif command == 'chest':
        bitcoins += int(number)
        print(f"You found {number} bitcoins.")
    else:
        health -= int(number)
        if health > 0:
            print(f"You slayed {command}.")
        else:
            is_dead = True
            break

if is_dead:
    print(f"You died! Killed by {command}.")
    print(f'Best room: {best_room}')
else:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f'Health: {health}')