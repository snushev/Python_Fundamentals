command = input()
exams = {}

while command != "exam finished":
    command_parts = command.split('-')
    username = command_parts[0]
    language = command_parts[1]

    if language == "banned":
        for lang in exams:
            if username in exams[lang]:
                del exams[lang][username]
        command = input()
        continue

    points = int(command_parts[2])

    if language not in exams:
        exams[language] = {}

    if username in exams[language]:
        if points > exams[language][username]:
            exams[language][username] = points
    else:
        exams[language][username] = points

    command = input()

print('Results:')
for users in exams.values():
    for username, points in users.items():
        print(f'{username} | {points}')
print('Submissions:')
for language, users in exams.items():
    print(f'{language}: {len(users)}')