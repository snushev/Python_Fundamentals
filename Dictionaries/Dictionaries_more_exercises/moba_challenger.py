players = {}

while True:
    command = input()

    if command == "Season end":
        break

    if "->" in command:
        player, position, skill = command.split(' -> ')
        skill = int(skill)
        if player not in players:
            players[player] = {}
        if position not in players[player]:
            players[player][position] = skill
        elif skill > players[player][position]:
            players[player][position] = skill

    elif " vs " in command:
        player1, player2 = command.split(' vs ')
        if player1 in players and player2 in players:
            common_positions = set(players[player1].keys()) & set(players[player2].keys())
            total_points_player1 = sum(players[player1].values())
            total_points_player2 = sum(players[player2].values())
            if common_positions:
                if total_points_player1 > total_points_player2:
                    del players[player2]
                elif total_points_player1 < total_points_player2:
                    del players[player1]

sorted_users = sorted(players.items(), key=lambda player_: (-sum(player_[1].values()), player_[0]))

for user, position in sorted_users:
    print(f'{user}: {sum(players[user].values())} skill')
    sorted_positions = sorted(position.items(), key=lambda pos_: (-pos_[1], pos_[0]))
    for pos, points in sorted_positions:
        print(f'- {pos} <::> {points}')