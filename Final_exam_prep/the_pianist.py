number_of_pieces = int(input())
pieces = {}

for i in range(number_of_pieces):
    piece, composer, key = input().split('|')
    pieces[piece] = {}
    pieces[piece]["composer"] = composer
    pieces[piece]["key"] = key

while True:
    piece = input()
    if piece == "Stop":
        break

    command = piece.split('|')
    parts = command[0]
    if parts == "Add":
        piece = command[1]
        composer = command[2]
        key = command[3]
        if piece not in pieces:
            pieces[piece] = {}
            pieces[piece]["composer"] = composer
            pieces[piece]["key"] = key
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif parts == "Remove":
        piece = command[1]
        if piece in pieces:
            del pieces[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif parts == "ChangeKey":
        piece = command[1]
        new_key = command[2]
        if piece in pieces:
            pieces[piece]["key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for piece, info in pieces.items():
    print(f"{piece} -> Composer: {info['composer']}, Key: {info['key']}")
