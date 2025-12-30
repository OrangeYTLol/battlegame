import sys, pygame
from entities.player import player
from map.tileManager import TileManager

class Battle:
    def __init__(self):
        global FPS, BLK
        pygame.init()
        self.tm = TileManager(self)
        SCALE = 5
        self.width = self.tm.columns * 16 * SCALE
        self.height = self.tm.rows * 16 * SCALE
        self.window = pygame.display.set_mode((self.width, self.height))
        self.screen = pygame.display.get_surface()
        pygame.display.set_caption("Battle")
        self.player1 = player(self)
        FPS = 30
        BLK = (0, 0, 0)
        
    def run(self):
        clock = pygame.time.Clock()
        while True:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            self.window.fill(BLK)
            self.tm.drawMap()
            self.player1.updateSprite()
            self.screen.blit(pygame.font.Font(None, 18).render(f"{clock.get_fps():2.0f} FPS" , True, (255, 255, 255)), (10, 10)) #on-screen FPS counter
            pygame.display.flip()
