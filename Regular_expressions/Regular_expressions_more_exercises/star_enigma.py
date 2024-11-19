import re

number_of_messages = int(input())
attack = []
destroy = []

for message in range(number_of_messages):
    current_message = input()

    regex = r"(?i)[star]"
    matches = re.findall(regex, current_message)
    special_num = len(matches)
    new_message = ""
    for char in current_message:
        updated_char = ord(char) - special_num
        new_message += chr(updated_char)

    new_regex = r".*?@(?P<planet>[A-Z][a-z]+)[^@:!\->]*:(?P<population>\d+)[^@:!\->]*!(?P<command>[AD])![^@:!\->]*->(?P<soldiers>\d+)"
    new_matches = re.match(new_regex, new_message)
    if not new_matches:
        continue

    planet = new_matches.group("planet")
    population = int(new_matches.group("population"))
    command = new_matches.group("command")
    soldiers = int(new_matches.group("soldiers"))

    if command == "A":
        attack.append(planet)
    elif command == "D":
        destroy.append(planet)

updated_attack_list = sorted(attack)
updated_destroy_list = sorted(destroy)

print(f"Attacked planets: {len(updated_attack_list)}")
for planet in updated_attack_list:
    print(f"-> {planet}")
print(f"Destroyed planets: {len(updated_destroy_list)}")
for planet in updated_destroy_list:
    print(f"-> {planet}")
