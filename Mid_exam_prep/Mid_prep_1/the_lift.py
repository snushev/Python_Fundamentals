people_waiting = int(input())
current_state_of_the_lift = list(map(int, input().split()))
max_seats = 4

for index, state in enumerate(current_state_of_the_lift):
    while state < 4:
        if people_waiting == 0:
            break
        state += 1
        people_waiting -= 1
    current_state_of_the_lift[index] = state

if people_waiting == 0:
    print("The lift has empty spots!")
    print(" ".join(map(str, current_state_of_the_lift)))

else:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(" ".join(map(str, current_state_of_the_lift)))