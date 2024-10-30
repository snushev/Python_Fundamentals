person = input()
phonebook = {}
while "-" in person:
    name, number = person.split("-")
    phonebook[name] = number
    person = input()

num = int(person)
for i in range(num):
    searched_name = input()
    if searched_name in phonebook:
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f'Contact {searched_name} does not exist.')