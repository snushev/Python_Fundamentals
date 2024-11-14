import re

date = input()
regex = r"\b(?P<Day>\d{2})([-/.])(?P<Month>[A-Z][a-z]{2})\2(?P<Year>\d{4})\b"
matches = re.finditer(regex, date)


for date in matches:
    date_dict = date.groupdict()
    keys_list = list(date_dict.keys())
    print(f"{keys_list[0]}: {date_dict['Day']}, {keys_list[1]}: {date_dict['Month']}, {keys_list[2]}: {date_dict['Year']}")