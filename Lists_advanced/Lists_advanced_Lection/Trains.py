wagons = int(input())
people_in_wagons = [0 for people in range(wagons)]

command = input().split()

while command[0] != "End":
    if command[0] == "add":
        number_of_people = int(command[1])
        people_in_wagons[-1] += number_of_people
    elif command[0] == "insert":
        index = int(command[1])
        number_of_people = int(command[2])
        people_in_wagons[index] += number_of_people
    elif command[0] == "leave":
        index = int(command[1])
        people_in_wagons[index] -= int(command[2])
    command = input().split()

else:
    print(people_in_wagons)