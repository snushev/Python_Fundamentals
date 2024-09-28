deck = input().split(" ")
shuffles = int(input())

for shuffle in range(shuffles):
    midpoint = len(deck) // 2
    first_half = deck[:midpoint]
    second_half = deck[midpoint:]

    shuffled_deck = []
    for card_index in range(len(first_half)):
        shuffled_deck.append(first_half[card_index])
        shuffled_deck.append(second_half[card_index])
    deck = shuffled_deck
print(deck)