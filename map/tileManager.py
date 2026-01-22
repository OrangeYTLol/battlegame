from map.tile import Tile
import yaml, pygame

class TileManager:
    def __init__(self, screen):
        #Screen object for attributes
        self.screen = screen
        #Amount of rows and columns on the screen
        self.rows = 8
        self.columns = 12
        #Define tile collision, entity collision, and player collision
        self.collision_group = pygame.sprite.Group()
        self.entity_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        #Load a default map
        self.loadMap("start")
    
    def loadMap(self, map):
        """
        Loads a map into memory
        """
        #Load map files
        tiles = open("./assets/maps/" + map + "/tiles.txt").read().split("\n") #Split the tiles.txt file into a list by line
        properties = yaml.safe_load(open("./assets/maps/" + map + "/mapproperties.yaml", "r")) #Load map properties
        self.map = [[[] for _ in range(self.rows)] for _ in range(self.columns)] #Create list where the tiles will get sorted into
        #Loop through the tiles in map
        for i in range(len(tiles)):
            #Use the dictionary as a constructor for a tile object and load the images into the object
            tiles[i] = Tile(eval(tiles[i]))
            tiles[i].getSprites("./assets/maps/" + map + "/tile.keys") if properties["tileKeys"] else tiles[i].getSprites()
            #Scale each sprite
            for j in range(len(tiles[i].sprites)):
                tiles[i].sprites[j] = tiles[i].sp.scaleImage(tiles[i].sprites[j])
            self.map[tiles[i].col-1][tiles[i].row-1].append(tiles[i])
    
    def drawMap(self):
        #Loop through tiles in map
        for i in range(self.columns):
            for j in range(self.rows):
                for tile in self.map[i][j]:
                    tile.updateSprite() #Update tile's spriteCounter
                    #Get current image
                    image = tile.sprites[tile.spriteNum-1]
                    rect = image.get_rect()
                    #Get pixel coordinates (column/row * tileSize * SCALE)
                    rect.x, rect.y = tile.col * rect.width, tile.row * rect.height
                    #Draw the image to the screen
                    self.screen.screen.blit(image, rect)