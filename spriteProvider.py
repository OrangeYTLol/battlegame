import pygame.image

class spriteProvider:
    def __init__(self, sprites, sheet):
        self.sprites = sprites
        self.sheet = pygame.image.load(f"./sprites/{sheet}.png")
        self.getSprites()
    def getSprites(self):
        spritelist = {}
        for sprite in self.sprites:
            [[(0, 0), (16, 16), "sprite1"], []]