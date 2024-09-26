numbers = int(input())
positive_list = []
negative_list = []


for _ in range(numbers):
    num = int(input())
    if num >= 0:
        positive_list.append(num)
    elif num < 0:
        negative_list.append(num)


positive_count = len(positive_list)
sum_of_negatives = sum(negative_list)

print(positive_list)
print(negative_list)
print(f"Count of positives: {positive_count} \nSum of negatives: {sum_of_negatives}")