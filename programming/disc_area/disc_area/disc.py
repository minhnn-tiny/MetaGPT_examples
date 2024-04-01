## disc.py
from typing import List, Tuple

class Disc:
    def __init__(self, x: float, y: float, radius: float):
        self.x = x
        self.y = y
        self.radius = radius

    def get_area(self, other: 'Disc') -> float:
        """
        Calculates the area of the intersection between two discs.

        Args:
            other: The other disc.

        Returns:
            The area of the intersection between the two discs.
        """

        # Calculate the distance between the centers of the two discs.
        dx = self.x - other.x
        dy = self.y - other.y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        # If the distance between the centers of the two discs is greater than the sum of their radii, then there is no intersection.
        if distance > self.radius + other.radius:
            return 0.0

        # Calculate the area of the intersection.
        area = 0.0
        if distance <= abs(self.radius - other.radius):
            area = min(self.radius, other.radius) ** 2 * math.pi
        else:
            a = (self.radius ** 2 - other.radius ** 2 + distance ** 2) / (2 * distance)
            h = (self.radius ** 2 - a ** 2) ** 0.5
            area = (a * h + other.radius ** 2 * math.acos(a / other.radius)) * 2

        return area
