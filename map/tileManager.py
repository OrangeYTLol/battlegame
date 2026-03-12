from map.tile import Tile
import yaml, importlib
import concurrent.futures
from threading import Thread

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
        self.mapName = ""
        self.mapProperties = {}
    
    def loadMap(self, name: str):
        """
        Loads a map into memory
        """
        self.mapName = name
        #Load map files
        self.tiles = open("./assets/maps/" + self.mapName + "/tiles.txt").read().split("\n") #Split the tiles.txt file into a list by line
        self.mapProperties = yaml.safe_load(open("./assets/maps/" + self.mapName + "/mapproperties.yaml", "r")) #Load map properties
        self.collision_group = []
        
        tiles = Thread(target=self.loadTiles)
        entities = Thread(target=self.loadEntities)
        tiles.start() 
        tiles.join()
        entities.start()
        #entities.join()
        
    def createTile(self, i):
        #Use the dictionary as a constructor for a tile object and load the images into the object
        constructor = eval(self.tiles[i])
        self.tiles[i] = Tile(constructor, "./assets/maps/" + self.mapName + "/tile.keys") if self.mapProperties["tileKeys"] else Tile(constructor)
        #Add tile to collision list if collision attribute is set to true
        if self.tiles[i].hasCollision:
            self.collision_group.append(self.tiles[i].rect)
    
    def loadTiles(self):
        #Loop through the tiles in the map
        tiles = range(len(self.tiles))
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(self.createTile, tiles)
        
    def loadEntities(self):
        self.entities = []
        if len(self.mapProperties["entities"]):
            entities = importlib.import_module("assets.maps."+ self.mapName + ".mapentities")
            for entity in self.mapProperties["entities"]:
                entity = getattr(entities, entity)
                self.entities.append(entity(self.screen))
    
    def drawMap(self):
        """
        Draws a map onto the screen
        """
        #Loop through tiles in map
        for tile in self.tiles:
            try:
                tile.updateSprite() #Update tile's spriteCounter
                #Get current image
                image = tile.sp.scaleImage(tile.getSprites()[tile.spriteNum-1])
                rect = image.get_rect()
                #Get pixel coordinates (column/row * tileSize * SCALE)
                rect.x, rect.y = tile.col * rect.width, tile.row * rect.height
                #Draw the image to the screen
                self.screen.screen.blit(image, rect)
            except:
                pass
                #print("WARNING: Tile failed to load")
        for entity in self.entities:
            try:
                entity.update()
            except:
                print("WARNING: Entity failed to update")