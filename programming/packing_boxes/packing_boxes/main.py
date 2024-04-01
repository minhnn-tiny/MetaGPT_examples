import sys
from typing import List

from box import Box
from solution import Solution


def main() -> None:
    """
    The main function that reads the input and calls the solution.
    """
    boxes = []
    for line in sys.stdin:
        boxes.append(Box(int(line)))

    solution = Solution(boxes)
    result = solution.solve()
    print(result)


if __name__ == "__main__":
    main()
