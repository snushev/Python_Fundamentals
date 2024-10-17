number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

total_bonus = 0
max_bonus = 0
attendances = 0

for student in range(number_of_students):
    attendance_of_each_student = int(input())
    if number_of_lectures > 0:
        total_bonus = attendance_of_each_student / number_of_lectures * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = round(total_bonus)
        attendances = attendance_of_each_student

print(f"Max Bonus: {max_bonus}.")
print(f"The student has attended {attendances} lectures.")
