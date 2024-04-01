## main.py
from typing import List, Tuple

class Main:
    def __init__(self, nums: List[int], requests: List[Tuple[int, int, int]]):
        self.nums = nums
        self.requests = requests

    def solve(self):
        for l, v, k in self.requests:
            magic_integer = self.get_magic_integer(l, v)
            if len(magic_integer) < k:
                print("So sad")
            else:
                print(magic_integer[k - 1])

    def get_magic_integer(self, l: int, v: int) -> str:
        magic_integer = ""
        while l > 0:
            if l % 2 == 1:
                magic_integer = str(v % 10) + magic_integer
            v //= 10
            l //= 2
        return magic_integer

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    requests = []
    for _ in range(int(input())):
        l, v, k = [int(x) for x in input().split()]
        requests.append((l, v, k))
    main = Main(nums, requests)
    main.solve()
