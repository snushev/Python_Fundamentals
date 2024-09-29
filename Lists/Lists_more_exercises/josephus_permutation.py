people = input().split(' ')
k = int(input())
killed = []
index = 0

while len(people) > 0:

    index = (index + k - 1) % len(people)
    killed.append(int(people[index]))
    people.pop(index)

print(f'[{",".join(map(str, killed))}]')