def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def check_draw(board):
    return all(all(cell != " " for cell in row) for row in board)

def make_move(board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        try:
            row, col = map(int, input(f"Player {current_player}, enter your move (row and column): ").split())
        except ValueError:
            print("Invalid input. Please enter row and column as numbers.")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid move. Row and column must be between 0 and 2.")
            continue

        if not make_move(board, row, col, current_player):
            print("Invalid move. The cell is already occupied.")
            continue

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

tic_tac_toe()
