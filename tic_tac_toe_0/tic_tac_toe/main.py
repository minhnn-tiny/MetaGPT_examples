import game

def main():
    """
    The main function of the tic-tac-toe game.
    """

    # Create a new game object.
    game_obj = game.Game()

    # Print the initial game board.
    print_board(game_obj)

    # While the game is not over, get the player's move and update the game board.
    while not game_obj.winner:
        # Get the player's move.
        move = get_player_move()

        # Update the game board.
        game_obj.make_move(move[0], move[1])

        # Print the updated game board.
        print_board(game_obj)

    # Print the winner of the game.
    print("The winner is:", game_obj.winner)

def print_board(game_obj):
    """
    Prints the current state of the game board.
    """

    # Get the game board.
    board = game_obj.board

    # Print the top row of the board.
    print("  ", end="")
    for i in range(3):
        print(f" {i + 1}", end="")
    print()

    # Print the middle row of the board.
    print("  +---+---+---+")
    for i in range(3):
        print(f"{i + 1} |", end="")
        for j in range(3):
            if board[i][j] is None:
                print("   |", end="")
            else:
                print(f" {board[i][j]} |", end="")
        print()

    # Print the bottom row of the board.
    print("  +---+---+---+")

def get_player_move():
    """
    Gets the player's move.

    Returns:
        A tuple containing the row and column of the player's move.
    """

    # Get the player's input.
    move = input("Enter your move (row, column): ")

    # Convert the player's input to a tuple.
    move = tuple(int(x) for x in move.split(","))

    # Return the player's move.
    return move

if __name__ == "__main__":
    main()
