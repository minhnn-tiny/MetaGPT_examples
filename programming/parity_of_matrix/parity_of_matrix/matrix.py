class Matrix:
    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        self.prefix_sum_rows = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        self.prefix_sum_cols = [[0] * len(matrix) for _ in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.prefix_sum_rows[i][j] = matrix[i][j]
                if i > 0:
                    self.prefix_sum_rows[i][j] += self.prefix_sum_rows[i - 1][j]
                if j > 0:
                    self.prefix_sum_cols[i][j] += self.prefix_sum_cols[i][j - 1]

    def get_sum(self, x1: int, y1: int, x2: int, y2: int) -> int:
        sum = self.prefix_sum_rows[x2][y2]
        if x1 > 0:
            sum -= self.prefix_sum_rows[x1 - 1][y2]
        if y1 > 0:
            sum -= self.prefix_sum_cols[x2][y1 - 1]
        if x1 > 0 and y1 > 0:
            sum += self.prefix_sum_rows[x1 - 1][y1 - 1]
        return sum

    def remove_row_col(self, x: int, y: int):
        for i in range(x, len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self.prefix_sum_rows[i][j] -= self.matrix[x][j]
                if i > 0:
                    self.prefix_sum_rows[i][j] += self.prefix_sum_rows[i - 1][j]
        for i in range(len(self.matrix)):
            for j in range(y, len(self.matrix[0])):
                self.prefix_sum_cols[i][j] -= self.matrix[i][y]
                if j > 0:
                    self.prefix_sum_cols[i][j] += self.prefix_sum_cols[i][j - 1]
        self.matrix[x].pop(y)
        for row in self.matrix[x + 1:]:
            row.pop(y)

    def get_parity(self, x: int, y: int) -> str:
        sum = self.get_sum(0, 0, len(self.matrix) - 1, len(self.matrix[0]) - 1)
        sum -= self.get_sum(0, 0, x - 1, len(self.matrix[0]) - 1)
        sum -= self.get_sum(0, 0, len(self.matrix) - 1, y - 1)
        sum += self.get_sum(0, 0, x - 1, y - 1)
        return "Even" if sum % 2 == 0 else "Odd"
