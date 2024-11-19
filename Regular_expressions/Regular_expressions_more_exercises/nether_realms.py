import re

daemons = input().split(',')
daemons_dict = {}
for daemon in daemons:
    daemon = daemon.strip()
    daemons_dict[daemon] = {}
    regex_letters = r'[^0-9\.\+\-\*\/]'
    matches = re.findall(regex_letters, daemon)
    health = sum([ord(x) for x in matches])
    daemons_dict[daemon]['health'] = health
    regex_numbers = r'(-?\d+(\.\d+)?)'
    matches1 = re.findall(regex_numbers, daemon)
    base_damage = 0
    for match in matches1:
        base_damage += float(match[0])

    multiply = 1
    divide = 1
    for char in daemon:
        if char == '*':
            base_damage *= 2
        elif char == '/':
            base_damage /= 2
    daemons_dict[daemon]['damage'] = f"{base_damage:.2f}"

sorted_dict = dict(sorted(daemons_dict.items()))
for daemon, info in sorted_dict.items():
    print(f"{daemon} - {info['health']} health, {info['damage']} damage")
