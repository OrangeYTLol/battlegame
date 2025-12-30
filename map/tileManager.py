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
            self.map[i].getSprites()
            for j in range(len(self.map[i].sprites)):
                self.map[i].sprites[j] = self.map[i].sp.scaleImage(self.map[i].sprites[j])
    
    def drawMap(self):
        for tile in self.map:
            image = tile.sprites[tile.spriteNum-1]
            rect = image.get_rect()
            rect.x, rect.y = tile.col * rect.width, tile.row * rect.height
            self.screen.screen.blit(image, rect)