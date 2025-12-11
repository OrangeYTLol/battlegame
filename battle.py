import random
import time
import sys, pygame
class battle:
    def __init__(self):
        global FPS, BLK
        pygame.init()
        self.size = 1280, 720
        self.window = pygame.display.set_mode(size)
        self.screen = pygame.display.get_surface()
        self.pygame.display.set_caption("Battle")
        FPS = 10
        BLK = (0, 0, 0)

    def run(self):
        while True:
            self.clock = pygame.time.Clock()
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            self.window.fill(BLK)
            pygame.draw.rect(self.window, BLK)
            pygame.display.flip()
