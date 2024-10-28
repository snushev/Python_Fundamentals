old_genres = input().split(' | ')
command = input()

while command != "Stop!":
    command_parts = command.split()
    action = command_parts[0]

    if action == "Join":
        genre = command_parts[1]
        if genre not in old_genres:
            old_genres.append(genre)
    elif action == "Drop":
        genre = command_parts[1]
        if genre in old_genres:
            old_genres.remove(genre)
    elif action == "Replace":
        old_genre = command_parts[1]
        new_genre = command_parts[2]
        if old_genre in old_genres and new_genre not in old_genres:
            index = old_genres.index(old_genre)
            old_genres[index] = new_genre
    elif action == "Prefer":
        index1 = int(command_parts[1])
        index2 = int(command_parts[2])
        if 0 <= index1 < len(old_genres) and 0 <= index2 < len(old_genres):
            old_genres[index1], old_genres[index2] = old_genres[index2], old_genres[index1]

    command = input()

print(" ".join(old_genres))