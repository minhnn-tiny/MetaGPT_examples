class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.turn = player1

    def play(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.turn
            self.turn = self.player1 if self.turn == self.player2 else self.player2

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]

        return None

    def __str__(self):
        return '\n'.join([' '.join(row) for row in self.board])
