command = input()
courses = {}
while command != 'end':
    action = command.split(' : ')
    course = action[0]
    student = action[1]

    if course not in courses:
        courses[course] = []
    courses[course].append(student)

    command = input()

for course, students in courses.items():
    print(f"{course}: {len(students)}")
    for student in students: 
        print(f"-- {student}")