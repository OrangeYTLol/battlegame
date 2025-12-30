from entities.spriteProvider import SpriteProvider

class Tile:
    def __init__(self, attributes):
        #Tile format: {"col": int, "row": int, tileID: str, "tileIndex": int, "layer": int, "flags": list}
        self.col = attributes["col"] - 1
        self.row = attributes["row"] - 1
        self.tileID = attributes["tileID"]
        self.tileIndex = attributes["tileIndex"]
        self.layer = attributes["layer"]
        self.flags = attributes["flags"]
        self.sp = SpriteProvider()
        self.spriteNum = 1
        self.spriteTime = 8
        self.spriteCounter = 1
    
    def updateSprite(self):
        spriteCount = len(self.sprites)
        self.spriteCounter += 1
        if self.spriteCounter > self.spriteTime:
            if self.spriteNum < spriteCount:
                self.spriteNum += 1
            else:
                self.spriteNum = 1
            self.spriteCounter = 1

    def getSprites(self):
        tiles = eval(open("./assets/maps/tile.keys").read())
        tile = tiles[self.tileID][self.tileIndex][1]
        sheet = tiles[self.tileID][self.tileIndex][0]
        
        self.sp.loadSheet(sheet)
        self.sprites = self.sp.getSprites(tile)