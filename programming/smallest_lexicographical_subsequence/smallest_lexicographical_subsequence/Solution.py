class Solution:
    def __init__(self, string: str, k: int):
        self.string = string
        self.k = k
        self.result = ""

    def solve(self) -> str:
        """
        Finds the smallest lexicographical subsequence of the given length.

        :return: The smallest lexicographical subsequence.
        """
        used = set()
        for char in self.string:
            if len(self.result) == self.k:
                break
            if char not in used and (not self.result or char <= self.result[-1]):
                self.result += char
                used.add(char)
        return self.result
