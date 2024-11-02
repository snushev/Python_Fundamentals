dwarfs = {}

while True:
    command = input()

    if command == "Once upon a time":
        break

    dwarf_name, dwarf_hat_color, dwarf_physics = command.split(' <:> ')
    dwarf_physics = int(dwarf_physics)

    key = (dwarf_name, dwarf_hat_color)

    if key in dwarfs:
        if dwarf_physics > dwarfs[key][1]:
            dwarfs[key] = dwarf_physics
    dwarfs[key] = (dwarf_hat_color, dwarf_physics)

print(dwarfs)
