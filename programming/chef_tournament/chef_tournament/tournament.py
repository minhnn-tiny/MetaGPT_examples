import random
from typing import List

from chef import Chef


class Tournament:
    def __init__(self, chefs: List[Chef]):
        """
        Initializes a tournament with a list of chefs.

        Args:
            chefs: A list of chefs.
        """
        self.chefs = chefs

    def simulate(self) -> List[Chef]:
        """
        Simulates the tournament process and returns the final two chefs.

        Returns:
            A list of the final two chefs.
        """
        while len(self.chefs) > 2:
            # Randomly select two chefs for each cook-off.
            chef1 = random.choice(self.chefs)
            chef2 = random.choice(self.chefs)

            # Update the number of prize tokens each chef has.
            if chef1.get_prize_tokens() > chef2.get_prize_tokens():
                chef1.set_prize_tokens(chef1.get_prize_tokens() + 1)
            else:
                chef2.set_prize_tokens(chef2.get_prize_tokens() + 1)

            # Remove the losing chef from the tournament.
            self.chefs.remove(chef1 if chef1.get_prize_tokens() < chef2.get_prize_tokens() else chef2)

        return self.chefs

    def get_expected_difference(self) -> float:
        """
        Calculates the expected difference in prize tokens between the final two competitors.

        Returns:
            The expected difference in prize tokens.
        """
        # Calculate the expected number of prize tokens for each chef.
        expected_tokens = [chef.get_prize_tokens() for chef in self.chefs]

        # Calculate the expected difference in prize tokens.
        expected_difference = abs(expected_tokens[0] - expected_tokens[1])

        return expected_difference
