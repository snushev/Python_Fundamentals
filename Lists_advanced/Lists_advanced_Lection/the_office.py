employees = list(map(int, input().split()))
happiness_factor = int(input())

new_employees_happiness = [happiness * happiness_factor for happiness in employees]
average_happiness = sum(new_employees_happiness) / len(new_employees_happiness)

filtered_employees = list(filter(lambda x: x > average_happiness, new_employees_happiness))

if len(filtered_employees) >= len(new_employees_happiness) / 2:
    print(f"Score: {len(filtered_employees)}/{len(new_employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(filtered_employees)}/{len(new_employees_happiness)}. Employees are not happy!")