from entities.spriteProvider import SpriteProvider

class Tile:
    def __init__(self, attributes):
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
        try: self.changeLevelTrigger = attributes["changeLevelTo"] 
        except: pass
        try: self.existsWhenFlags = attributes["existsWhen"]
        except: pass
        try: self.hasCollision = self.collision
        except: raise AttributeError
    
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

    def getSprites(self, keys = "./assets/maps/tile.keys"):
        #Open tile keys as a dictionary to get tile image constructors and spritesheet
        tiles = eval(open(keys).read())
        tile = tiles[self.tileID][self.tileIndex][1]
        sheet = tiles[self.tileID][self.tileIndex][0]
        
        #Load spritesheet into spriteProvider and sprites into self.sprites
        self.sp.loadSheet(sheet)
        self.sprites = self.sp.getSprites(tile)