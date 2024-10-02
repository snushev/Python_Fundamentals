numbers = list(map(float, input().split()))
absolute_list = []

for num in numbers:
    absolute_list.append(abs(num))

print(absolute_list)