initial_energy = float(input())
terrain = input()
mountains = 0

while terrain != "Journey ends here!":
    if terrain == "mountain":
        mountains += 1
        initial_energy -= 10
        if mountains == 9:
            print(f"The character reached the legendary artifact with {initial_energy:.2f} energy left.")
            break
    elif terrain == "desert":
        initial_energy -= 15
    elif terrain == "forest":
        initial_energy += 7
    if initial_energy <= 0:
        print(f"The character is too exhausted to carry on with the journey.")
    terrain = input()

if terrain == "Journey ends here!" and initial_energy > 0:
    print(f"The character could not find all the pieces and needs {3 - mountains // 3} more to complete the legendary artifact.")


