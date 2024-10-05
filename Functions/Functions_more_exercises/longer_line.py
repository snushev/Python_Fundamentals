import math


def distance_from_center(x, y):
    return math.sqrt(x ** 2 + y ** 2)


def coordinates(x, y):
    return f'({math.floor(x)}, {math.floor(y)})'


def closest_point(x1, y1, x2, y2):
    distance1 = distance_from_center(x1, y1)
    distance2 = distance_from_center(x2, y2)

    if distance1 <= distance2:
        return coordinates(x1, y1), coordinates(x2, y2)
    else:
        return coordinates(x2, y2), coordinates(x1, y1)


def line(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


first_line_x1 = float(input())
first_line_y1 = float(input())
first_line_x2 = float(input())
first_line_y2 = float(input())
second_line_x1 = float(input())
second_line_y1 = float(input())
second_line_x2 = float(input())
second_line_y2 = float(input())

first_line = line(first_line_x1, first_line_y1, first_line_x2, first_line_y2)
second_line = line(second_line_x1, second_line_y1, second_line_x2, second_line_y2)

if first_line >= second_line:
    result = closest_point(first_line_x1, first_line_y1, first_line_x2, first_line_y2)
    print("".join(result))

else:
    result = closest_point(second_line_x1, second_line_y1, second_line_x2, second_line_y2)
    print("".join(result))