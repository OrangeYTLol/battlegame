from map.tile import Tile

class TileManager:
    def __init__(self, screen):
        self.screen = screen
        self.loadMap("start")
        self.rows = 8
        self.columns = 12
    
    def loadMap(self, map):
        self.map = open("./assets/maps/" + map + ".map").read().split("\n")
        for i in range(len(self.map)):
            self.map[i] = Tile(eval(self.map[i]))
    
    def drawMap(self):
        for tile in self.map:
            image = tile.getSprites()[tile.spriteNum-1]
            image = tile.sp.scaleImage(image)
            rect = image.get_rect()
            rect.x, rect.y = tile.col * rect.width, tile.row * rect.height
            self.screen.screen.blit(image, rect)