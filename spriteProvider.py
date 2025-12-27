import pygame.image

class SpriteProvider:
    def getSprites(self, sprites):
        for i in range(len(sprites)):
            sprites[i] = self.sheet.subsurface(pygame.Rect(sprites[i]))
        return sprites
    
    def loadSheet(self, sheet):
        self.sheet = pygame.image.load("./sprites/" + sheet + ".png")