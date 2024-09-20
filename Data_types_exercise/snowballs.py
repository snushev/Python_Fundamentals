total_snowballs = int(input())
best_snowball = 0
best_ball_weight = 0
best_ball_time = 0
best_ball_quality = 0

for i in range(total_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    overall = (weight // time) ** quality

    if overall > best_snowball:
        best_snowball = overall
        best_ball_weight = weight
        best_ball_time = time
        best_ball_quality = quality

print(f'{best_ball_weight} : {best_ball_time} = {best_snowball} ({best_ball_quality})')