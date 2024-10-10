notes = [0] * 10

while True:
    task = input().split('-')
    if task[0] == 'End':
        break
    note = int(task[0]) - 1
    description = task[1]
    notes[note] = description

notes = [note for note in notes if note != 0]
print(notes)
