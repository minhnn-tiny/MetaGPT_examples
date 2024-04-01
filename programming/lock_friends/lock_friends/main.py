from solution import Solution

def main():
    """
    The main function of the program.
    """

    # Read the input from the console.
    friends = list(map(int, input().split()))
    houses = list(map(int, input().split()))
    times = []
    for _ in range(len(friends)):
        times.append(list(map(int, input().split())))

    # Create a solution object and solve the problem.
    solution = Solution(friends, houses, times)
    result = solution.solve()

    # Print the result to the console.
    print(*result)

if __name__ == "__main__":
    main()
