class Game:
    def __init__(self, num_players, num_rounds):
        self.num_players = num_players
        self.num_rounds = num_rounds
        self.players = []
        for i in range(num_players):
            self.players.append(Player())

    def play_round(self):
        for player in self.players:
            player.play()

    def get_winner(self):
        winner = None
        for player in self.players:
            if player.score > winner.score:
                winner = player
        return winner
