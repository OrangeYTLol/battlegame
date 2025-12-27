import sys, pygame
from player import player
class Battle:
    def __init__(self):
        global FPS, BLK, player1
        pygame.init()
        self.width = 1280
        self.height = 720
        self.window = pygame.display.set_mode((self.width, self.height))
        self.screen = pygame.display.get_surface()
        pygame.display.set_caption("Battle")
        player1 = player(self)
        FPS = 30
        BLK = (0, 0, 0)

    def run(self):
        while True:
            self.clock = pygame.time.Clock()
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            self.window.fill(BLK)
            player1.updateSprite()
            pygame.display.flip()
