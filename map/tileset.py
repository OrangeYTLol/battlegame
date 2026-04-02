from entities.spriteProvider import SpriteProvider

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
        self.current_map = open(file).read().split(";")
        print(self.current_map)
