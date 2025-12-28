from entities.spriteProvider import SpriteProvider

class Tile:
    def __init__(self, tileID):
        #tileID: "id;index;layer" EX. "t1;1;1"
        self.tileset = tileID[:2]
        self.tileNum = int(tileID[3])
        self.layer = tileID[5]
        self.sp = SpriteProvider()
        self.spriteNum = 1
    
    def getSprites(self):
        tiles = {
            "b1": {
                1: ("tiles/b1", [(0, 0, 16, 16)])
            },
            "t1": {
                1: ("tiles/b1", [(17, 0, 16, 16)])
            }
        }
        tile = tiles[self.tileset][self.tileNum][1]
        sheet = tiles[self.tileset][self.tileNum][0]
        
        self.sp.loadSheet(sheet)
        return self.sp.getSprites(tile)
        
        
        