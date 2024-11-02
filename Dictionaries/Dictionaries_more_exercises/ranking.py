contests_dict = {}
while True:
    data = input()
    if data == "end of contests":
        break
    contest, password = data.split(':')
    contests_dict[contest] = password

users_dict = {}
while True:
    data = input()
    if data == "end of submissions":
        break
    contest, password, username, points = data.split('=>')
    points = int(points)
    if contest in contests_dict and contests_dict[contest] == password:
        if username not in users_dict:
            users_dict[username] = {}
        if contest not in users_dict[username] or points > users_dict[username][contest]:
            users_dict[username][contest] = points

best_user = ""
best_total_points = 0
for user, contests in users_dict.items():
    total_points = sum(contests.values())
    if total_points > best_total_points:
        best_user = user
        best_total_points = total_points

print(f"Best candidate is {best_user} with total {best_total_points} points.")
print("Ranking:")
for user in sorted(users_dict):
    print(user)
    for contest, points in sorted(users_dict[user].items(), key=lambda x: -x[1]):
        print(f"#  {contest} -> {points}")
