from map.tile import Tile
import yaml, importlib

class TileManager:
    def __init__(self, screen):
        #Screen object for drawing
        self.screen = screen
        #Amount of rows and columns on the screen
        self.rows = 8
        self.columns = 12
        #Define a list for tiles with collision
        self.collision_group = []
        self.tiles = []
        self.entities = []
        #Load a default map
        self.loadMap("start")
    
    def loadMap(self, name: str):
        """
        Loads a map into memory
        """
        #Load map files
        self.tiles = open("./assets/maps/" + name + "/tiles.txt").read().split("\n") #Split the tiles.txt file into a list by line
        properties = yaml.safe_load(open("./assets/maps/" + name + "/mapproperties.yaml", "r")) #Load map properties
        self.collision_group = []
        #Loop through the tiles in the map
        for i in range(len(self.tiles)):
            #Use the dictionary as a constructor for a tile object and load the images into the object
            self.tiles[i] = Tile(eval(self.tiles[i]), "./assets/maps/" + name + "/tile.keys") if properties["tileKeys"] else Tile(eval(self.tiles[i]))
            #Add tile to collision list if collision attribute is set to true
            if self.tiles[i].hasCollision:
                self.collision_group.append(self.tiles[i].rect)
        self.entities = []
        if len(properties["entities"]):
            entities = importlib.import_module("assets.maps."+ name + ".mapentities")
            for entity in properties["entities"]:
                entity = getattr(entities, entity)
                self.entities.append(entity(self.screen))
    
    def drawMap(self):
        """
        Draws a map onto the screen
        """
        #Loop through tiles in map
        for tile in self.tiles:
            tile.updateSprite() #Update tile's spriteCounter
            #Get current image
            image = tile.sp.scaleImage(tile.getSprites()[tile.spriteNum-1])
            rect = image.get_rect()
            #Get pixel coordinates (column/row * tileSize * SCALE)
            rect.x, rect.y = tile.col * rect.width, tile.row * rect.height
            #Draw the image to the screen
            self.screen.screen.blit(image, rect)
        for entity in self.entities:
            entity.update()