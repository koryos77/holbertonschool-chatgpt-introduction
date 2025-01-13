#!/usr/bin/python3

def print_board(board):
    """Prints the Tic Tac Toe board."""
    print("\nTic Tac Toe Board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there is a winner in the game. A winner is defined as
    three consecutive marks (X or O) in a row, column, or diagonal.
    
    Parameters:
    board (list of list of str): The 3x3 game board.

    Returns:
    bool: True if there is a winner, False otherwise.
    """
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True  # Row
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True  # Column
    
    if board[0][0] == board[1][1] == board[2][2] != " ":  # Main diagonal
        return True
    
    if board[0][2] == board[1][1] == board[2][0] != " ":  # Anti diagonal
        return True
    
    return False

def check_draw(board):
    """
    Checks if the game is a draw (i.e., the board is full and no winner).
    
    Parameters:
    board (list of list of str): The 3x3 game board.

    Returns:
    bool: True if the game is a draw, False otherwise.
    """
    for row in board:
        if " " in row:
            return False  # If there is any empty space, it's not a draw
    return True

def get_valid_input(player, board):
    """
    Gets a valid row and column input from the player.
    Ensures the input is a valid number, within bounds, and the cell is empty.

    Parameters:
    player (str): The current player ("X" or "O").
    board (list of list of str): The 3x3 game board.

    Returns:
    tuple: A tuple (row, col) representing the player's move.
    """
    while True:
        try:
            # Get row input
            row = int(input(f"Player {player}, enter row (0, 1, 2): "))
            if row not in [0, 1, 2]:
                print("Invalid row! Please enter a number between 0 and 2.")
                continue
            
            # Get column input
            col = int(input(f"Player {player}, enter column (0, 1, 2): "))
            if col not in [0, 1, 2]:
                print("Invalid column! Please enter a number between 0 and 2.")
                continue
            
            # Check if the chosen spot is already taken
            if board[row][col] != " ":
                print("That spot is already taken! Please choose another one.")
                continue
            
            # Confirm the action before proceeding
            confirm = input(f"Player {player}, you chose row {row} and column {col}. Do you want to place your mark here? (y/n): ").lower()
            if confirm == 'y':
                return row, col
            else:
                print("Action cancelled, choose another spot.")
                continue
        except ValueError:
            print("Invalid input! Please enter numeric values between 0 and 2.")
        except EOFError:
            print("\nGame exited.")
            exit()

def tic_tac_toe():
    """
    Main function that runs the Tic Tac Toe game.
    Alternates between two players (X and O) until there is a winner, draw, or the game is exited.
    """
    # Initialize the 3x3 board
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    print("Welcome to Tic Tac Toe!")
    print("Rules: Players take turns to place 'X' or 'O' on the board. The first player to align three marks in a row, column, or diagonal wins. Use Ctrl + d to exit the game !")
    
    while True:
        print_board(board)
        
        # Get a valid move from the player
        row, col = get_valid_input(player, board)
        board[row][col] = player

        # Check for a winner
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break
        
        # Check for a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Alternate the player
        player = "O" if player == "X" else "X"

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
