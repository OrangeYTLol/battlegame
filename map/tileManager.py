from map.tile import Tile

class TileManager:
    def __init__(self, screen):
        self.screen = screen
        self.loadMap("test")
        self.rows = 8
        self.columns = 12
    
    def loadMap(self, map):
        self.map = open("./assets/maps/" + map + ".map").read().split()
        for i in range(len(self.map)):
            self.map[i] = Tile(self.map[i])
    
    def drawMap(self):
        row = 0
        col = 0
        for tile in self.map:
            image = tile.getSprites()[tile.spriteNum-1]
            image = tile.sp.scaleImage(image)
            rect = image.get_rect()
            rect.x, rect.y = col * rect.width, row * rect.height
            col += 1
            if col >= self.columns:
                row += 1
                col = 0
            self.screen.screen.blit(image, rect)