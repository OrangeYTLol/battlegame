from map.tile import Tile

class TileManager:
    def __init__(self, screen):
        #Screen object for attributes
        self.screen = screen
        #Load a default map
        self.loadMap("start")
        #Amount of rows and columns on the screen
        self.rows = 8
        self.columns = 12
    
    def loadMap(self, map):
        #Split the map file into a list by line
        self.map = open("./assets/maps/" + map + ".map").read().split("\n")
        #Loop through the tiles in map
        for i in range(len(self.map)):
            #Use the dictionary as a constructor for a tile object and load the images into the object
            self.map[i] = Tile(eval(self.map[i]))
            self.map[i].getSprites()
            #Scale each sprite
            for j in range(len(self.map[i].sprites)):
                self.map[i].sprites[j] = self.map[i].sp.scaleImage(self.map[i].sprites[j])
    
    def drawMap(self):
        #Loop through tiles in map
        for tile in self.map:
            tile.updateSprite() #Update tile's spriteCounter
            #Get current image
            image = tile.sprites[tile.spriteNum-1]
            rect = image.get_rect()
            #Get pixel coordinates (column/row * tileSize * SCALE)
            rect.x, rect.y = tile.col * rect.width, tile.row * rect.height
            #Draw the image to the screen
            self.screen.screen.blit(image, rect)