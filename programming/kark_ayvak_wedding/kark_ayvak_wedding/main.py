from game import Game

def main():
    """
    The main function of the program.
    """

    # Create a new game object.
    game = Game([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [0.5, 0.5])

    # Calculate the expected number of hearts in each cell.
    expected_hearts = game.calculate_expected_hearts()

    # Print the expected number of hearts in each cell.
    for row in expected_hearts:
        for heart in row:
            print(heart, end=" ")
        print()

if __name__ == "__main__":
    main()
