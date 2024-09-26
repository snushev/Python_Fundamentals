team_a = 11
team_b = 11

sequence = input()
cards_list = sequence.split(' ')
processed_cards = []


for card in cards_list:
    if card in processed_cards:
        continue
    processed_cards.append(card)
    if card[0] == 'A':
        team_a -= 1
    elif card[0] == 'B':
        team_b -= 1
    if team_a < 7 or team_b < 7:
        print(f'Team A - {team_a}; Team B - {team_b}')
        print("Game was terminated")
        break
else:
    print(f'Team A - {team_a}; Team B - {team_b}')