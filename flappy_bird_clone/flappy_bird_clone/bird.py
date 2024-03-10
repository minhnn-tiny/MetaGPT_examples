import pygame

class Bird:
    def __init__(self):
        # Setting default values for the bird's position and velocity using Vector2 for efficiency
        self.position = pygame.math.Vector2(100, 250)  # Default starting position (x, y) as a mutable Vector2
        self.velocity = 0.0  # Default starting velocity
        self.gravity = 0.5  # Gravity effect on the bird
        self.flap_strength = -10  # The upward force when the bird flaps
        self.bird_image = pygame.image.load('assets/bird.png')  # Load the bird image
        # Initialize the bird's rect with the new position Vector2
        self.bird_rect = self.bird_image.get_rect(center=(self.position.x, self.position.y))

    def flap(self):
        # This method applies an upward force to the bird when it flaps
        self.velocity = self.flap_strength

    def update(self):
        # This method updates the bird's position
        self.velocity += self.gravity  # Apply gravity to velocity
        self.position.y += self.velocity  # Update position based on velocity using Vector2

        # Prevent the bird from moving off-screen
        if self.position.y > 600:  # Assuming the window height is 600 pixels
            self.position.y = 600
            self.velocity = 0  # Reset velocity to prevent bouncing effect
        elif self.position.y < 0:
            self.position.y = 0
            self.velocity = 0  # Reset velocity to prevent bouncing effect

        # Update the bird's rect position for collision detection
        self.bird_rect.center = self.position

    def draw(self, screen):
        # This method draws the bird on the screen
        screen.blit(self.bird_image, self.bird_rect)
