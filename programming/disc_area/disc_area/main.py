from disc import Disc

def main():
    """
    Main function to calculate the total area covered by a set of discs.

    Args:
        None

    Returns:
        None
    """

    # Create a list of discs.
    discs = [
        Disc(0, 0, 1),
        Disc(1, 1, 1),
        Disc(2, 2, 1),
    ]

    # Calculate the total area covered by the discs.
    total_area = 0
    for disc1 in discs:
        for disc2 in discs:
            if disc1 != disc2:
                total_area += disc1.get_area(disc2)

    # Print the total area covered by the discs.
    print(total_area)

if __name__ == "__main__":
    main()
