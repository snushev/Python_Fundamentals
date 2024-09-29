race = input().split()

left_racer_time = 0
right_racer_time = 0

midpoint = (len(race) - 1) // 2
left_racer = race[:midpoint]
right_racer = race[midpoint + 1:][::-1]

for time in left_racer:
    if time == "0":
        left_racer_time = left_racer_time * 0.8
    else:
        left_racer_time += int(time)
for time in right_racer:
    if time == "0":
        right_racer_time *= 0.8
    else:
        right_racer_time += int(time)
if left_racer_time > right_racer_time:
    print(f'The winner is right with total time: {right_racer_time:.1f}')
else:
    print(f'The winner is left with total time: {left_racer_time:.1f}')

