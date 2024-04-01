from collections import defaultdict

class Main:
    def __init__(self):
        self.leaves = defaultdict(lambda: defaultdict(int))

    def main(self) -> int:
        n = int(input())
        for _ in range(n):
            type, color, num = input().split()
            self.leaves[type][color] += int(num)

        max_leaves = 0
        for type in self.leaves:
            for color in self.leaves[type]:
                max_leaves = max(max_leaves, self.leaves[type][color])

        return max_leaves

if __name__ == "__main__":
    main = Main()
    print(main.main())

