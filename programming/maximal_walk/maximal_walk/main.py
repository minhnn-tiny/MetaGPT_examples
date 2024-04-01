class Solution:
    def __init__(self, l: int, r: int):
        self.l = l
        self.r = r
        self.k = self.r - self.l + 1
        self.c = pow(self.k, 2, 1000000007)

    def solve(self):
        print(self.k, self.c)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        l, r = map(int, input().split())
        Solution(l, r).solve()
