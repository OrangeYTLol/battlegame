from entities.spriteProvider import SpriteProvider

class Tile:
    def __init__(self, tileID):
        self.tileset = tileID[:2]
        self.tileNum = int(tileID[3])
        self.layer = tileID[5]
    
    def getSprites(self):
        
        sp = SpriteProvider()
        tiles = {
            "b1": {
                1: ("tiles/tileset", [(0, 0, 16, 16)])
                }
        }
        tile = tiles[self.tileset][self.tileNum][1]
        sheet = tiles[self.tileset][self.tileNum][0]
        
        sp.loadSheet(sheet)
        return sp.getSprites(tile)
        
        
        