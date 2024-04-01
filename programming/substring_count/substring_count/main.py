from typing import List, Tuple
from collections import defaultdict

class Solution:
    def __init__(self, s: str, pairs: List[Tuple[int, int]]):
        self.s = s
        self.pairs = pairs

    def solve(self) -> List[int]:
        # Create a dictionary to store the count of substrings for each pair of integers.
        substring_counts = defaultdict(int)

        # Iterate over the pairs of integers.
        for pair in self.pairs:
            # Get the start and end indices of the substring.
            start, end = pair

            # Iterate over the substrings that start at the start index and end at the end index.
            for i in range(start, end + 1):
                for j in range(i, end + 1):
                    # Increment the count of the substring.
                    substring_counts[self.s[i:j+1]] += 1

        # Return the list of counts of substrings for each pair of integers.
        return [substring_counts[substring] for substring in self.s]
