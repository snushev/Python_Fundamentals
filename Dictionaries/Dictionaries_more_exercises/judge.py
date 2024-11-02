contests = {}
input_order = {}

while True:
    command = input()
    if command == "no more time":
        break
    username, contest, points = command.split(' -> ')
    points = int(points)

    if contest not in contests:
        contests[contest] = {}
        input_order[contest] = {}

    if username not in contests[contest]:
        contests[contest][username] = points
        input_order[contest][username] = len(input_order[contest])
    elif points > contests[contest][username]:
        contests[contest][username] = points

for contest, participants in contests.items():
    print(f'{contest}: {len(participants)} participants')
    sorted_participants = sorted(participants.items(),
                                 key=lambda item: (-item[1], item[0], input_order[contest][item[0]]))
    for index, (participant, points) in enumerate(sorted_participants):
        print(f'{index + 1}. {participant} <::> {points}')

individual_standings = {}
input_order_individual = {}
for key, value in contests.items():
    for participant, points in value.items():
        if participant not in individual_standings:
            individual_standings[participant] = 0
            input_order_individual[participant] = len(input_order_individual)
        individual_standings[participant] += points

print(f'Individual standings:')
sorted_individuals = sorted(individual_standings.items(),
                            key=lambda item: (-item[1], item[0], input_order_individual[item[0]]))
for i, (username, points) in enumerate(sorted_individuals, start=1):
    print(f'{i}. {username} -> {points}')
