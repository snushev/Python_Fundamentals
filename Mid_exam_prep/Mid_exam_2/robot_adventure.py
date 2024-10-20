def backward(city_grid_cells, total_points, new_command):
    start_index = int(new_command[1])
    steps = int(new_command[2])
    if start_index in range(len(city_grid_cells)):
        index = start_index - steps
        if index < 0:
            index = 0
        total_points += city_grid_cells[index]
        city_grid_cells[index] = 0
    return city_grid_cells, total_points


def forward(city_grid_cells, total_points, new_command):
    start_index = int(new_command[1])
    steps = int(new_command[2])
    if start_index in range(len(city_grid_cells)):
        index = start_index + steps
        if index >= len(city_grid_cells):
            index = len(city_grid_cells) - 1
        total_points += city_grid_cells[index]
        city_grid_cells[index] = 0
    return city_grid_cells, total_points


def step(city_grid_cells, total_points, command):
    new_command = command[1].split('$')
    if new_command[0] == 'Backward':
        city_grid_cells, total_points = backward(city_grid_cells, total_points, new_command)
    elif new_command[0] == 'Forward':
        city_grid_cells, total_points = forward(city_grid_cells, total_points, new_command)
    return city_grid_cells, total_points


def double(city_grid_cells, command):
    index = int(command[1])
    if index in range(len(city_grid_cells)):
        city_grid_cells[index] *= 2
    return city_grid_cells


def switch(city_grid_cells):
    return city_grid_cells[::-1]


def main():
    city_grid_cells = list(map(int,input().split('|')))
    command = input()
    total_points = 0

    while command != "Adventure over":
        command = command.split(' ')
        if command[0] == "Step":
            city_grid_cells, total_points = step(city_grid_cells, total_points, command)
        elif command[0] == "Double":
            city_grid_cells = double(city_grid_cells, command)
        elif command[0] == "Switch":
            city_grid_cells = switch(city_grid_cells)

        command = input()
    print(" - ".join(map(str, city_grid_cells)))


main()
