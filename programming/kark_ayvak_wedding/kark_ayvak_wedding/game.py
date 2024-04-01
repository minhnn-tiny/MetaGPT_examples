import typing
from typing import List

class Game:
    def __init__(self, grid: List[List[int]], hearts: List[int]) -> None:
        self.grid = grid
        self.hearts = hearts
        self.dp = [[0.0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    def calculate_expected_hearts(self) -> List[List[float]]:
        for i in range(len(self.grid) - 1, -1, -1):
            for j in range(len(self.grid[0]) - 1, -1, -1):
                if i == len(self.grid) - 1 and j == len(self.grid[0]) - 1:
                    self.dp[i][j] = self.hearts[i][j]
                else:
                    self.dp[i][j] = (
                        (self.dp[i + 1][j] + self.dp[i][j + 1] - self.dp[i + 1][j + 1] + self.hearts[i][j])
                        / (len(self.grid) * len(self.grid[0]) - i * len(self.grid[0]) - j)
                    )
        return self.dp

    def get_expected_hearts(self, i: int, j: int) -> float:
        return self.dp[i][j]
