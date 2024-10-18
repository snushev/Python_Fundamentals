list_of_integers = list(map(int, input().split()))

average_number = sum(list_of_integers) / len(list_of_integers)
greater_than_average = [num for num in list_of_integers if num > average_number]
sorted_list = sorted(greater_than_average, reverse=True)
if len(sorted_list) > 5:
    sorted_list = sorted_list[:5]

if sorted_list:
    print(" ".join(map(str, sorted_list)))
else:
    print("No")
