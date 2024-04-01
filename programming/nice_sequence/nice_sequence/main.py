from typing import List
from solution import Solution

def main():
    N, K, D = map(int, input().split())
    solution = Solution(N, K, D)
    print(solution.solve())

if __name__ == "__main__":
    main()
