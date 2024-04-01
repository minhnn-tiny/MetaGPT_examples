import random

class Chef:
    def __init__(self, name: str, prize_tokens: int):
        self._name = name
        self._prize_tokens = prize_tokens

    def get_name(self) -> str:
        return self._name

    def get_prize_tokens(self) -> int:
        return self._prize_tokens

    def set_prize_tokens(self, prize_tokens: int):
        self._prize_tokens = prize_tokens
