from typing import List
from collections import defaultdict

class Solution:
    def __init__(self, cooks: List[int], C: int, M: int):
        self.cooks = cooks
        self.C = C
        self.M = M
        self.dp = defaultdict(int)

    def solve(self) -> List[int]:
        self.dp[(0, 0)] = 1
        for i in range(len(self.cooks)):
            for j in range(self.C):
                self.dp[(i + 1, j)] = self.dp[(i, j)]
                if self.cooks[i] >= j + 1:
                    self.dp[(i + 1, j)] = max(self.dp[(i + 1, j)], self.dp[(i, j - 1)] + 1)

        res = []
        for j in range(self.C):
            if self.dp[(len(self.cooks), j)] <= self.M:
                res.append(j)

        return res
