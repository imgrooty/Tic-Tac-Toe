# Tic Tac Toe Game

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    return all([cell != " " for row in board for cell in row])

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    while True:
        print_board(board)
        row, col = map(int, input(f"Player {players[current_player]}, enter row and column (0-2): ").split())

        if board[row][col] == " ":
            board[row][col] = players[current_player]
            
            if check_win(board, players[current_player]):
                print_board(board)
                print(f"Player {players[current_player]} wins!")
                break

            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            
            current_player = 1 - current_player
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    tic_tac_toe()
          
