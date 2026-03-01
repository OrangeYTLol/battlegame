from entities.spriteProvider import SpriteProvider
from pygame import Rect

class Tile:
    """
    A Tile created from a .txt file containing a list of attributes with predetermined values
    """
    def __init__(self, attributes: dict, keys: str = "./assets/maps/tile.keys"):
        self.sp = SpriteProvider()
        self.spriteNum = 1 #Sprite index
        self.spriteTime = 8 #Time between sprite changes
        self.spriteCounter = 1 #Time since last sprite change
        self.hasCollision = False
        #Declare attributes based on dictionary constructor
        {"col": int, "row": int, "tileID": str, "tileIndex": int, "collision": bool, "changeLevelTo": str, "existsWhen": list} #Constructor format
        try:
            self.col = attributes["col"] - 1
            self.row = attributes["row"] - 1
            self.tileID = attributes["tileID"]
            self.tileIndex = attributes["tileIndex"]
            self.collision = attributes["collision"]
        except:
            raise AttributeError
        self.rect = Rect(self.col * 16 * self.sp.SCALE, self.row * 16 * self.sp.SCALE, 16 * self.sp.SCALE, 16 * self.sp.SCALE)
        try: self.changeLevelTrigger = attributes["changeLevelTo"] 
        except: pass
        try: self.existsWhenFlags = attributes["existsWhen"]
        except: pass
        try: self.hasCollision = self.collision
        except: raise AttributeError
        self.sprites = [] #List of sprites the tile will use that gets set when self.getSprites is run
        #Open tile keys as a dictionary to get tile image constructors and spritesheet name
        tiles = eval(open(keys).read())
        tile = tiles[self.tileID][self.tileIndex][1]
        #Get the file name of the spritesheet
        sheet = tiles[self.tileID][self.tileIndex][0]
        #Load spritesheet into spriteProvider and sprites into self.sprites
        self.sp.loadSheet(sheet)
        self.sprites = tile
    
    def updateSprite(self):
        """
        increment spriteNum every {spriteTime} game ticks
        """
        spriteCount = len(self.sprites) #Get amount of sprites

        #Increment spriteNum if spriteCounter is equal to spriteTime
        self.spriteCounter += 1
        if self.spriteCounter > self.spriteTime:
            if self.spriteNum < spriteCount:
                self.spriteNum += 1
            else:
                self.spriteNum = 1
            self.spriteCounter = 1  

    def getSprites(self):
        """
        Gets a list of image objects from a list of pygame.Rect object constructors
        """
        return self.sp.getSprites(self.sprites)