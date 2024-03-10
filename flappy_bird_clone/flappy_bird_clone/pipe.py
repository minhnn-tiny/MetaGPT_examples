import pygame
from bird import Bird  # Ensure this import does not create circular dependencies

class Pipe:
    """
    Represents an obstacle pipe in the game with a position and a gap size.
    """
    def __init__(self, position=(0, 0), gap_size=200):
        """
        Initializes the Pipe object with validation for position and gap_size.

        Args:
            position (tuple): The initial position of the pipe as a tuple (x, y).
            gap_size (int): The size of the gap between the upper and lower pipes.
        """
        # Validate position and gap_size
        if not isinstance(position, tuple) or not isinstance(gap_size, int):
            raise ValueError("Invalid position or gap_size type. Position must be a tuple, and gap_size must be an integer.")
        if gap_size <= 0:
            raise ValueError("gap_size must be positive.")

        self.position = position
        self.gap_size = gap_size
        self.image_upper = pygame.transform.flip(pygame.image.load("assets/pipe.png"), False, True)
        self.image_lower = pygame.image.load("assets/pipe.png")
        self.rect_upper = self.image_upper.get_rect(topleft=(self.position[0], self.position[1] - self.gap_size - self.image_upper.get_height()))
        self.rect_lower = self.image_lower.get_rect(topleft=(self.position[0], self.position[1]))

    def move(self, speed=5):
        """
        Moves the pipe to the left by a specified speed and updates the position attribute.

        Args:
            speed (int): The speed at which the pipe moves to the left.
        """
        # Move the rectangles
        self.rect_upper.move_ip(-speed, 0)
        self.rect_lower.move_ip(-speed, 0)
        # Update the position attribute based on the new position of the rectangles
        self.position = self.rect_lower.topleft

    def check_collision(self, bird: Bird) -> bool:
        """
        Checks if the bird has collided with either the upper or lower pipe.

        Args:
            bird (Bird): The bird object to check for collisions.

        Returns:
            bool: True if there is a collision, False otherwise.
        """
        bird_rect = pygame.Rect(bird.position[0], bird.position[1], bird.image.get_width(), bird.image.get_height())
        return bird_rect.colliderect(self.rect_upper) or bird_rect.colliderect(self.rect_lower)

    def draw(self, screen):
        """
        Draws the upper and lower pipes on the screen.

        Args:
            screen (pygame.Surface): The surface on which to draw the pipes.
        """
        screen.blit(self.image_upper, self.rect_upper.topleft)
        screen.blit(self.image_lower, self.rect_lower.topleft)
