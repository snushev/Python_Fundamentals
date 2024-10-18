initial_energy = int(input())
command = input()
wins = 0

while True:
    if command == "End of battle":
        print(f"Won battles: {wins}. Energy left: {initial_energy}")
        break
    else:
        distance = int(command)
        if initial_energy < distance:
            print(f"Not enough energy! Game ends with {wins} won battles and {initial_energy} energy")
            break
        initial_energy -= distance
        wins += 1
        if wins % 3 == 0:
            initial_energy += wins
    command = input()
