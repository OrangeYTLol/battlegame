import pygame

class SpriteProvider:
    def getSprites(self, sprites):
        for i in range(len(sprites)):
            sprites[i] = self.sheet.subsurface(pygame.Rect(sprites[i]))
        return sprites
    
    def loadSheet(self, sheet):
        self.sheet = pygame.image.load("./assets/sprites/" + sheet + ".png")
        
    def scaleImage(self, image):
        SCALE = 5
        return pygame.transform.scale(image, (image.get_rect().width * SCALE, image.get_rect().height * SCALE))