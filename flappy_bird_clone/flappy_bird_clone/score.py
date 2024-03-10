## score.py

class Score:
    def __init__(self):
        self.current_score = 0  # Initialize current score to 0
        self.highest_score = 0  # Initialize highest score to 0

    def update(self, points=1):
        """
        Update the current score by a specific number of points.
        By default, it increases the score by 1 point.

        Args:
            points (int): The number of points to add to the current score.
        """
        self.current_score += points
        # Update the highest score if the current score is greater
        if self.current_score > self.highest_score:
            self.highest_score = self.current_score

    def reset(self):
        """
        Reset the current score to 0.
        """
        self.current_score = 0

    def get_current_score(self) -> int:
        """
        Get the current score.

        Returns:
            int: The current score.
        """
        return self.current_score

    def get_highest_score(self) -> int:
        """
        Get the highest score.

        Returns:
            int: The highest score.
        """
        return self.highest_score
