# Function to print the current state of the board
def print_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# Function to check if the given player has won the game
def check_winner(board, player):
    # List of all possible winning combinations (row, column, diagonals)
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8),     # Rows
        (0,3,6), (1,4,7), (2,5,8),     # Columns
        (0,4,8), (2,4,6)               # Diagonals
    ]
    # Check if any win condition is satisfied by the current player
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == player:
            return True
    return False

# Function to check if the board is full and the game is a draw
def check_draw(board):
    return all(place in ['x', 'o'] for place in board)

# Main function to run the Tic-Tac-Toe game
def main():
    # Initial board with numbers 1–9 for user reference
    board = ['1','2','3','4','5','6','7','8','9']
    current_player = 'o'  # Starting player

    while True:
        print_board(board)  # Show the current board

        # Ask the player to choose a cell
        move = input(f"Player {current_player}, choose a cell (1-9): ")

        # Validate input
        if not move.isdigit() or int(move) not in range(1, 10):
            print("Invalid move, Please enter a valid move between (1-9)!")
            continue

        move = int(move) - 1  # Convert to 0-based index

        # Check if the selected cell is already taken
        if board[move] in ['x', 'o']:
            print("Cell already taken, Please choose another one.")
            continue

        # Mark the cell with the current player's symbol
        board[move] = current_player

        # Check if the current player has won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check if the game is a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch to the other player
        current_player = 'x' if current_player == 'o' else 'o'

# Start the game
main()
