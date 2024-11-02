from collections import Counter

dwarfs = {}

while True:
    command = input()

    if command == "Once upon a time":
        break

    dwarf_name, dwarf_hat_color, dwarf_physics = command.split(' <:> ')
    dwarf_physics = int(dwarf_physics)

    key = (dwarf_name, dwarf_hat_color)

    if key not in dwarfs or dwarf_physics > dwarfs[key][1]:
        dwarfs[key] = (dwarf_hat_color, dwarf_physics)

color_counts = Counter(color for name, (color, physics) in dwarfs.items())

sorted_dwarfs = sorted(
    dwarfs.items(),
    key=lambda item: (-item[1][1], -color_counts[item[1][0]])
)

for (name, hat_color), (hat_color, physics) in sorted_dwarfs:
    print(f"({hat_color}) {name} <-> {physics}")
