

population = list(map(int, input().split(", ")))
minimum_wealth = int(input())
richest_person = max(population)
richest_person_index = population.index(richest_person)

if sum(population) < (minimum_wealth * len(population)):
    print("No equal distribution possible")
else:
    for index, person in enumerate(population):
        if person < minimum_wealth:
            diff = minimum_wealth - person
            population[richest_person_index] -= diff
            population[index] += diff
            richest_person = max(population)
            richest_person_index = population.index(richest_person)
    print(population)

