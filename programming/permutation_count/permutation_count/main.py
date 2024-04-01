from solution import Solution

def main():
    """
    The main function.
    """

    # Get the input.
    n = int(input())

    # Create a solution object.
    solution = Solution()

    # Count the number of permutations.
    count = solution.count_permutations(n)

    # Print the output.
    print(count)

if __name__ == "__main__":
    main()
