#!/usr/bin/python3

def print_board(board):
    """Prints the Tic Tac Toe board."""
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
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """
    Main function that runs the Tic Tac Toe game.
    Alternates between two players (X and O) until there is a winner or the game ends in a draw.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while not check_winner(board):
        print_board(board)
        
        # Get valid row input
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                if row not in [0, 1, 2]:
                    print("Invalid row! Please enter 0, 1, or 2.")
                else:
                    break
            except ValueError:
                print("Invalid input! Please enter a numeric value between 0 and 2.")
        
        # Get valid column input
        while True:
            try:
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                if col not in [0, 1, 2]:
                    print("Invalid column! Please enter 0, 1, or 2.")
                else:
                    break
            except ValueError:
                print("Invalid input! Please enter a numeric value between 0 and 2.")
        
        # Check if the chosen spot is already taken
        if board[row][col] == " ":
            board[row][col] = player
            # Alternate the player after a valid move
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("That spot is already taken! Try again.")
    
    print_board(board)
    # Correct winner announcement
    if player == "X":
        print("Player O wins!")
    else:
        print("Player X wins!")

# Run the game
tic_tac_toe()
