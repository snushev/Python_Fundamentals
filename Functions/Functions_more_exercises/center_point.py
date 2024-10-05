import math


def distance_from_center(x, y):
    return math.sqrt(x ** 2 + y ** 2)


def coordinates(x, y):
    return f'({math.floor(x)}, {math.floor(y)})'


def closest_point(x1, y1, x2, y2):
    distance1 = distance_from_center(x1, y1)
    distance2 = distance_from_center(x2, y2)

    if distance1 <= distance2:
        return coordinates(x1, y1)
    else:
        return coordinates(x2, y2)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(closest_point(x1, y1, x2, y2))