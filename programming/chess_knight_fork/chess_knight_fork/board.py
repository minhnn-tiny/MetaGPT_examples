class Board:
    def __init__(self, n: int, queens: List[Tuple[int, int]]):
        """
        Initialize the board with the given size and queens positions.

        Args:
            n (int): The size of the board.
            queens (List[Tuple[int, int]]): The positions of the queens on the board.
        """
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        self.queens = queens
        self.knights = []

    def is_safe(self, x: int, y: int) -> bool:
        """
        Check if the given position is safe for a knight to move to.

        Args:
            x (int): The x-coordinate of the position.
            y (int): The y-coordinate of the position.

        Returns:
            bool: True if the position is safe, False otherwise.
        """
        for queen in self.queens:
            if queen[0] == x or queen[1] == y or abs(queen[0] - x) == abs(queen[1] - y):
                return False
        return True

    def can_fork(self, x: int, y: int) -> bool:
        """
        Check if a knight placed at the given position can fork at least two queens.

        Args:
            x (int): The x-coordinate of the position.
            y (int): The y-coordinate of the position.

        Returns:
            bool: True if the knight can fork at least two queens, False otherwise.
        """
        count = 0
        for queen in self.queens:
            if queen[0] == x or queen[1] == y or abs(queen[0] - x) == abs(queen[1] - y):
                count += 1
        return count >= 2

    def count_forking_positions(self) -> int:
        """
        Count the number of positions on the board where a knight can fork at least two queens.

        Returns:
            int: The number of forking positions.
        """
        count = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.is_safe(i, j) and self.can_fork(i, j):
                    count += 1
        return count
