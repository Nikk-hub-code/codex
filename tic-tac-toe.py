import random

print(f"Thank you for having a look towards my Tic-Tac-Toe game.\n\nHope you would like it.\n\nIt's basically a multiplayer game where who gets a chance to play with X and who gets a chance to play with O is randomly generated.")
print("\nPress enter to continue.....")

usr_input = input()
if usr_input == '':
    plyr1 = input(f"Enter the name of first player= ").upper()
    plyr2 = input(f"Enter the name of second player= ").upper()

# random symbol assigning to both the players
symbol = ['X', '0']
plyr1_symbol = random.choice(symbol)
plyr2_symbol = ''
plyr2_symbol = '0' if plyr1_symbol == 'X' else 'X'

print(f"{plyr1}= {plyr1_symbol}\n{plyr2}= {plyr2_symbol}")

# Print the board.
def show_board(board):
    for row in board:
        print(" | ".join(row))
        print("-"*10)

# This function check for the winner.
def winner(board, player):
    # checking Rows-wise.
    for row in board:
        if all(place == player for place in row):
            return True
    # Checking Columns-wise.
    for column in range(3):
        if all(board[row][column] == player for row in range(3)):
            return True
    # Checking diagonals-wise.
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

# Check whether the game is draw or not.
def board_full(board):
    return all(all(place != " " for place in row) for row in board)

# Actual game defined.
def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_plyr = plyr1 if plyr1_symbol == 'X' else plyr2
    current_plyr_symbol = plyr1_symbol if current_plyr == plyr1 else plyr2_symbol
    loop = False

    # Game will not end until anyone of them wins or the match is draw.
    while not loop:
        show_board(board)
        # This particular part in Try Except block because to track whether the user has entered or not entered valid input.
        try:
            # Ask current player to choose where they wants to place their symbol.
            user_row_choice = int(input(f"{current_plyr} Enter the row(0, 1 or 2)= "))
            user_col_choice = int(input(f"{current_plyr} Enter the column(0, 1 or 2)= "))
            if board[user_row_choice][user_col_choice] == " ":
                board[user_row_choice][user_col_choice] = current_plyr_symbol
            else:
                print("It's not the valid spot.\nChoose different spot.")
                continue
        except (ValueError, IndexError):
            print("Invalid Input.\nEnter number between 0 and 2.")
            continue
        
        # Check if anyone of them have won in either of the case.
        if winner(board, current_plyr_symbol):
            show_board(board)
            print(f"{current_plyr} wins.")
            loop = True
        # Check for the draw case.
        elif board_full(board):
            show_board(board)
            print("Match Draw.")
            loop = True
        else:
            # Switch the player.
            current_plyr = plyr2 if current_plyr == plyr1 else plyr1
            current_plyr_symbol = plyr2_symbol if current_plyr_symbol == plyr1_symbol else plyr1_symbol

# Game is called.
tic_tac_toe()