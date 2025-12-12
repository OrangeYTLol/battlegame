import sys, pygame
from player import player
class battle:
    def __init__(self):
        global FPS, BLK, player1
        pygame.init()
        self.size = 1280, 720
        self.window = pygame.display.set_mode(self.size)
        self.screen = pygame.display.get_surface()
        pygame.display.set_caption("Battle")
        player1 = player(self)
        FPS = 10
        BLK = (0, 0, 0)

    def run(self):
        while True:
            self.clock = pygame.time.Clock()
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            self.window.fill(BLK)
            #pygame.draw.rect(self.window, BLK)
            player1.updateSprite()
            pygame.display.flip()
