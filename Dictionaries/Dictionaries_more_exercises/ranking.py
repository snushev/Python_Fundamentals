contests = input()
contests_dict = {}

while contests != "end of contests":
    contest_name, password = contests.split(':')
    contests_dict[contest_name] = password
    contests = input()

data = input()
users_dict = {}
while data != "end of submissions":
    contest_name, password, username, points = data.split('=>')
    points = int(points)
    if contest_name in contests_dict and contests_dict[contest_name] == password:
        if username not in users_dict:
            users_dict[username] = {}
        if contest_name not in users_dict[username] or points > users_dict[username][contest_name]:
            users_dict[username][contest_name] = points
    data = input()

total_points = {}
max_points = 0
best_user = ""

for user in users_dict:
    total_points[user] = sum(users_dict[user].values())
    if total_points[user] > max_points:
        max_points = total_points[user]
        best_user = user

print(f"Best candidate is {best_user} with total {max_points} points.")
print("Ranking:")
for user in users_dict:
    print(f'{user}')
    for contest in users_dict[user]:
        print(f'#  {contest} -> {users_dict[user][contest]}')