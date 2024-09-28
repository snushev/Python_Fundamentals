offers = list(map(int, input().split(', ')))
num_beggars = int(input())

beggars_sums = [0] * num_beggars


for i in range(len(offers)):
    beggar_index = i % num_beggars
    beggars_sums[beggar_index] += offers[i]

print(beggars_sums)
