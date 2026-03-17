"""
TODO:
Comment code
Optimize tile rendering
"""
#from game.battle import Battle #Custom object for pygame window and display stuff
import sys, pygame
from entities.player import Player
from map.tileManager import TileManager

class Runner:
    def __init__(self):
        #Make constants private instead of local
        global FPS, BLK
        #Initialize Pygame
        pygame.init()
        #Create a TileManager object for map loading & drawing
        self.tm = TileManager(self)
        self.SCALE = 5 #Screen upscale amount
        #Create screen and window
        self.width = self.tm.columns * 16 * self.SCALE
        self.height = self.tm.rows * 16 * self.SCALE
        self.window = pygame.display.set_mode((self.width, self.height))
        self.screen = pygame.display.get_surface()
        pygame.display.set_caption("Game")
        #Create player object
        self.player1 = Player(self)
        #Constants
        FPS = 30
        BLK = (0, 0, 0)
        
    def run(self, map: str):
        """
        The main function responsible for game flow; checking if player quits and updating the map.
        """
        self.tm.loadMap(map)
        #Define clock
        clock = pygame.time.Clock()
        while True:
            #Limit FPS
            clock.tick(FPS)
            #Stop pygame when window closed
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            #Refresh screen
            self.window.fill(BLK)
            #Draw map and player to the screen
            self.tm.drawMap()
            self.player1.updateSprite()
            #self.screen.blit(pygame.font.Font(None, 18).render(f"{clock.get_fps():2.0f} FPS" , True, (255, 255, 255)), (10, 10)) #on-screen FPS counter
            pygame.display.flip()

game = Runner()
#Run game loop
game.run("start")