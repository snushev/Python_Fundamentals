number_of_pairs = int(input())
students_grades = {}

for pair in range(number_of_pairs):
    student_name = input()
    grade = float(input())

    if student_name not in students_grades:
        students_grades[student_name] = []
    students_grades[student_name].append(grade)

for student in students_grades:
    average_grade = sum(students_grades[student]) / len(students_grades[student])
    if average_grade >= 4.5:
        print(f"{student} -> {average_grade:.2f}")