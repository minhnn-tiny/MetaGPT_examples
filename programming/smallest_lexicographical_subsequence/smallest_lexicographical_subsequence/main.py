from typing import List
from solution import Solution

def main():
    """
    This is the main function.
    """

    # Get the input string and the length of the subsequence.
    string = input()
    k = int(input())

    # Create a Solution object and find the smallest lexicographical subsequence.
    solution = Solution(string, k)
    result = solution.solve()

    # Print the result.
    print(result)

if __name__ == "__main__":
    main()
