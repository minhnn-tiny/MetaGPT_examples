## game.py
import pygame
from bird import Bird
from pipe import Pipe
from score import Score
from sounds import Sounds

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 600))
        pygame.display.set_caption("Flappy Bird Clone")
        self.clock = pygame.time.Clock()
        self.running = True
        self.bird = Bird(velocity=0.0, position=(100, 300))
        self.pipes = [Pipe(position=(400, 0), gap_size=200)]
        self.score = Score(current_score=0, highest_score=0)
        self.sounds = Sounds()

    def add_pipe(self):
        if not self.pipes or self.screen.get_width() - self.pipes[-1].position[0] > 200:
            self.pipes.append(Pipe(position=(400, 0), gap_size=200))

    def remove_pipes(self):
        self.pipes = [pipe for pipe in self.pipes if pipe.position[0] > -pipe.width]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.flap()

    def run(self):
        while self.running:
            self.handle_events()

            self.screen.fill((135, 206, 235))  # Sky blue background
            self.bird.update()
            self.screen.blit(self.bird.image, self.bird.position)

            self.add_pipe()
            for pipe in self.pipes:
                pipe.move()
                self.screen.blit(pipe.upper_image, pipe.upper_position)
                self.screen.blit(pipe.lower_image, pipe.lower_position)
                if pipe.check_collision(self.bird):
                    self.sounds.play_sound('hit')
                    self.restart()

            self.remove_pipes()

            self.score.update()
            score_surface = self.score.font.render(f"Score: {self.score.current_score}", True, (255, 255, 255))
            self.screen.blit(score_surface, (10, 10))

            pygame.display.update()
            self.clock.tick(30)

    def restart(self):
        self.bird = Bird(velocity=0.0, position=(100, 300))
        self.pipes = [Pipe(position=(400, 0), gap_size=200)]
        self.score.reset()

if __name__ == "__main__":
    game = Game()
    game.run()
