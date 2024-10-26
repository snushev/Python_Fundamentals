size_of_a_side = float(input())
sheets_of_paper = int(input())
total_area = size_of_a_side * size_of_a_side * 6
area_covered = 0

for sheet in range(1, sheets_of_paper + 1):
    length = float(input())
    width = float(input())
    area_of_current_sheet = length * width
    if sheet % 3 == 0:
        area_of_current_sheet *= 0.75
    if sheet % 5 == 0:
        area_of_current_sheet = 0

    area_covered += area_of_current_sheet

if total_area > area_covered:
    percentage_covered = (area_covered / total_area) * 100
    print(f"You are out of paper!\n{100 - percentage_covered:.2f}% of the box is not covered.")
else:
    percentage_left = ((area_covered - total_area) / area_covered) * 100
    print(f"You've covered the gift box!\n{percentage_left:.2f}% wrap paper left.")
