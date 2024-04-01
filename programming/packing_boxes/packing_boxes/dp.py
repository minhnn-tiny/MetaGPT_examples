class Box:
    def __init__(self, size):
        self.size = size

class Solution:
    def __init__(self, boxes):
        self.boxes = boxes
        self.dp = [0] * (len(boxes) + 1)

    def solve(self):
        for i in range(1, len(self.boxes) + 1):
            self.dp[i] = min(self.dp[j] + self.dp[i - j] + self.boxes[j].size + self.boxes[i - j].size for j in range(1, i // 2 + 1))

        return self.dp[len(self.boxes)]
