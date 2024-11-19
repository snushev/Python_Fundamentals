import re

racers = input().split(", ")
race_info = {}

while True:
    info = input()
    if info == "end of race":
        break

    regex_name = r"([A-Za-z])"
    name = "".join(re.findall(regex_name, info))

    if name in racers:
        regex_distance = r'\d'
        distance = re.findall(regex_distance, info)
        total_distance = sum(map(int, distance))
        if name not in race_info:
            race_info[name] = 0
        race_info[name] += total_distance

sorted_dict_desc = sorted(race_info.items(), key=lambda item: item[1], reverse=True)

racers = []
counter = 0
for name, distance in sorted_dict_desc:
    if counter < 3:
        racers.append(name)
        counter += 1
    else:
        break

print(f"1st place: {racers[0]}")
print(f"2nd place: {racers[1]}")
print(f"3rd place: {racers[2]}")