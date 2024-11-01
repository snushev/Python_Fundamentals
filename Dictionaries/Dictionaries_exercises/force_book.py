command = input()
the_force = {}

while command != "Lumpawaroo":
    if "|" in command:
        side, user = command.split(' | ')

        user_found = False
        for users in the_force.values():
            if user in users:
                user_found = True
                break

        if not user_found:
            if side not in the_force:
                the_force[side] = []
            the_force[side].append(user)

    elif "->" in command:
        user, side = command.split(' -> ')

        for s, users in the_force.items():
            if user in users:
                users.remove(user)
                break

        if side not in the_force:
            the_force[side] = []

        the_force[side].append(user)
        print(f"{user} joins the {side} side!")

    command = input()

for side, users in the_force.items():
    if users:
        print(f"Side: {side}, Members: {len(users)}")
        for member in users:
            print(f"! {member}")