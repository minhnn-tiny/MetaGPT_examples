class Solution:
    def count_permutations(self, n: int) -> int:
        """
        Counts the number of permutations of [1, 2, ..., n] that satisfy the given property.

        Args:
            n: The number of elements in the permutation.

        Returns:
            The number of permutations that satisfy the given property.
        """

        # Create a 2D array to store the number of permutations that satisfy the given property and end with each element.
        dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

        # Initialize the base cases.
        dp[1][1] = 1
        dp[1][2] = 0

        # Compute the number of permutations that satisfy the given property and end with each element.
        for i in range(2, n + 1):
            for j in range(1, n + 2):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

        # Return the number of permutations that satisfy the given property and end with n.
        return dp[n][n]
