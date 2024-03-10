import pygame
import sys
from game import Game

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 600))
    pygame.display.set_caption("Flappy Bird Clone")
    
    clock = pygame.time.Clock()
    game = Game(screen)
    
    while True:
        game.handle_events()  # Encapsulated event handling
        game.run()
        
        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()
