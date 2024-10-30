data = input()

courses = {}

while ':' in data:
    name, id_, course = data.split(':')
    if course not in courses:
        courses[course] = {id_: name}
    else:
        courses[course][id_] = name
    data = input()

course_name = data.replace('_', ' ')
students = courses[course_name]

for id_, name in students.items():
    print(f"{name} - {id_}")