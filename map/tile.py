from entities.spriteProvider import SpriteProvider

class Tile:
    def __init__(self, attributes):
        #Declare attributes based on dictionary constructor
        #Tile format: {"col": int, "row": int, tileID: str, "tileIndex": int, "layer": int, "flags": list}
        self.col = attributes["col"] - 1
        self.row = attributes["row"] - 1
        self.tileID = attributes["tileID"]
        self.tileIndex = attributes["tileIndex"]
        self.layer = attributes["layer"]
        self.flags = attributes["flags"]
        self.sp = SpriteProvider()
        self.spriteNum = 1 #Sprite index
        self.spriteTime = 8 #Time between sprite changes
        self.spriteCounter = 1 #Time since last sprite change
    
    def updateSprite(self):
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
        #Open tile keys as a dictionary to get tile image constructors and spritesheet
        tiles = eval(open("./assets/maps/tile.keys").read())
        tile = tiles[self.tileID][self.tileIndex][1]
        sheet = tiles[self.tileID][self.tileIndex][0]
        
        #Load spritesheet into spriteProvider and sprites into self.sprites
        self.sp.loadSheet(sheet)
        self.sprites = self.sp.getSprites(tile)