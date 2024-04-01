## game.py
from typing import List, Dict, Any
from utils import get_timestamp

class Game:
    def __init__(self, name: str, players: List[str], start_time: float = get_timestamp()) -> None:
        self.name = name
        self.players = players
        self.start_time = start_time
        self.end_time: float = 0.0
        self.winner: str = ""

    def start(self) -> None:
        print(f"Game {self.name} started at {self.start_time}")

    def end(self, winner: str) -> None:
        self.end_time = get_timestamp()
        self.winner = winner
        print(f"Game {self.name} ended at {self.end_time} with winner {self.winner}")

    def get_info(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "players": self.players,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "winner": self.winner,
        }
