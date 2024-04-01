class Solution:
    def __init__(self, N: int, K: int, D: int):
        self.N = N
        self.K = K
        self.D = D
        self.dp = [[0] * (K + 1) for _ in range(N + 1)]

    def solve(self) -> int:
        for i in range(1, self.N + 1):
            for j in range(1, self.K + 1):
                for k in range(max(1, j - self.D), j + 1):
                    self.dp[i][j] += self.dp[i - 1][k]

        return sum(self.dp[self.N][j] for j in range(1, self.K + 1))
