"""
TODO:
Comment code
Optimize tile rendering
"""
#System functions & 2D Graphics functionality
import sys, pygame
#Player and tile manager classes
from entities.player import Player
from map.tileManager import TileManager

#Runner class for managing all of the game's functions
class Runner:
    def __init__(self):
        #Make constants private instead of local
        global FPS, BLK
        #Initialize Pygame
        pygame.init()
        #Create a TileManager object for map loading & drawing
        self.tm = TileManager(self)
        self.SCALE = 5 #Screen upscale amount
        #Create screen where all the sprites get drawn to
        self.width = self.tm.columns * 16 * self.SCALE
        self.height = self.tm.rows * 16 * self.SCALE
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Game")
        #Create a player object
        self.player1 = Player(self)
        #Constants
        FPS = 30
        BLK = (0, 0, 0)
        
    def run(self, map: str):
        """
        The main function responsible for the game loop and functions, limited by the FPS constant
        """
        self.tm.loadMap(map)
        #Define clock
        clock = pygame.time.Clock()
        #Game loop
        while True:
            #Limit FPS
            clock.tick(FPS)
            #Stop pygame when window closed
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
            #Refresh screen
            self.screen.fill(BLK)
            #Draw tiles, entities and player to the screen
            self.tm.drawMap()
            self.player1.update()
            #On-screen FPS counter for benchmarking
            #self.screen.blit(pygame.font.Font(None, 18).render(f"{clock.get_fps():2.0f} FPS" , True, (255, 255, 255)), (10, 10))
            #Apply changes to the screen
            pygame.display.flip()

#Create an instance of the runner class
game = Runner()
#Run game loop
game.run("start")