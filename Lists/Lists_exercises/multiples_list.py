factor = int(input())
count = int(input())
lis = []

for i in range(1, count + 1):
    lis.append(factor * i)

print(lis)