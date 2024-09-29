row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
row3 = list(map(int, input().split()))

board = [row1, row2, row3]

if board[0][0] == board[0][1] == board[0][2] != 0:
    winner = board[0][0]
elif board[1][0] == board[1][1] == board[1][2] != 0:
    winner = board[1][0]
elif board[2][0] == board[2][1] == board[2][2] != 0:
    winner = board[2][0]

elif board[0][0] == board[1][0] == board[2][0] != 0:
    winner = board[0][0]
elif board[0][1] == board[1][1] == board[2][1] != 0:
    winner = board[0][1]
elif board[0][2] == board[1][2] == board[2][2] != 0:
    winner = board[0][2]

elif board[0][0] == board[1][1] == board[2][2] != 0:
    winner = board[0][0]
elif board[0][2] == board[1][1] == board[2][0] != 0:
    winner = board[0][2]

else:
    winner = 0

if winner == 1:
    print("First player won")
elif winner == 2:
    print("Second player won")
else:
    print("Draw!")
