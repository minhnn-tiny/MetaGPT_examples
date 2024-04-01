from Solution import Solution

def main():
    """
    This is the main function.
    """

    # Get the input.
    default_rate = float(input())
    minutes = int(input())
    num_plans = int(input())
    plans = []
    for _ in range(num_plans):
        months, rate, cost = map(int, input().split())
        plans.append(Solution.Plan(months, rate, cost))

    # Solve the problem.
    solution = Solution(default_rate, minutes, plans)
    result = solution.solve()

    # Print the output.
    print(result)

if __name__ == "__main__":
    main()
