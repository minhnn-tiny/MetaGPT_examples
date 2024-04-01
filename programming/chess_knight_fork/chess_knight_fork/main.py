import board

def main():
    """
    The main function.
    """

    # Get the input.
    n = int(input())
    queens = []
    for i in range(n):
        x, y = map(int, input().split())
        queens.append((x, y))

    # Create the board.
    board = board.Board(n, queens)

    # Count the number of forking positions.
    count = board.count_forking_positions()

    # Print the output.
    print(count)

if __name__ == "__main__":
    main()
