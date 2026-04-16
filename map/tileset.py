from entities.spriteProvider import SpriteProvider
import yaml

class Tileset:
    def __init__(self, img: str, anim_speed: int, tiles: dict = {}):
        self.img = img
        self.tiles = tiles
        self.anim_speed = anim_speed
        self.sp = SpriteProvider()
        self.current_tiles = []
        self.sp.loadSheet(self.img)
        for key in tiles.keys():
            tiles[key] = self.sp.getSprites(tiles[key])
    
    def set_tile(self, num: int, frames: list):
        self.tiles[num] = self.sp.getSprites(frames)

    def load_tiles(self, file: str):
        self.current_map = open(file).read().split("\n")
        for i in range(len(self.current_map)):
            self.current_map[i] = self.current_map[i].split(";")
            while "" in self.current_map[i]:
                self.current_map[i].remove("")
    
    def update(self):
        settings = yaml.safe_load(open("./settings.yaml"))
        x = settings["cameraX"]
        y = settings["cameraY"]
        for i in range(0 + y, len(self.current_map)):
            for j in range(0 + x, len(self.current_map[i])):
                try:
                    image = self.sp.scaleImage(self.tiles[int(self.current_map[i][j])][0])
                    rect = image.get_rect()
                    #Get pixel coordinates (column/row * tileSize * SCALE)
                    rect.x, rect.y = (j - x) * rect.width, (i - y) * rect.height
                    #Draw the image to the screen
                    self.screen.screen.blit(image, rect)
                except: pass
