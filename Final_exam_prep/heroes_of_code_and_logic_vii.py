number_of_heroes = int(input())
heroes = {}

for hero in range(number_of_heroes):
    add_hero = input().split()
    hero_name = add_hero[0]
    hero_health = int(add_hero[1])
    hero_mana = int(add_hero[2])

    heroes[hero_name] = {"health": hero_health, "mana": hero_mana}

while True:
    command = input()
    if command == "End":
        break

    parts = command.split(' - ')
    action = parts[0]
    hero_name = parts[1]
    if action == "CastSpell":
        mana_needed = int(parts[2])
        spell_name = parts[3]
        if heroes[hero_name]["mana"] >= mana_needed:
            heroes[hero_name]["mana"] -= mana_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name]['mana']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif action == "TakeDamage":
        damage = int(parts[2])
        attacker = parts[3]
        heroes[hero_name]["health"] -= damage
        if heroes[hero_name]["health"] <= 0:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes[hero_name]
        else:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['health']} HP left!")
    elif action == "Recharge":
        mana_to_recharge = int(parts[2])
        initial_mana = heroes[hero_name]["mana"]
        heroes[hero_name]["mana"] += mana_to_recharge
        if heroes[hero_name]["mana"] > 200:
            mana_to_recharge = 200 - initial_mana
            heroes[hero_name]["mana"] = 200
        print(f"{hero_name} recharged for {mana_to_recharge} MP!")
    elif action == "Heal":
        healing_amount = int(parts[2])
        initial_health = heroes[hero_name]["health"]
        heroes[hero_name]["health"] += healing_amount
        if heroes[hero_name]["health"] > 100:
            healing_amount = 100 - initial_health
            heroes[hero_name]["health"] = 100

        print(f"{hero_name} healed for {healing_amount} HP!")

for hero, info in heroes.items():
    print(f"{hero}\n  HP: {info['health']}\n  MP: {info['mana']}")