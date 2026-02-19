import pygame

class SpriteProvider:
    def __init__(self):
        self.SCALE = 5 #Scale constant
    #Takes in a list with pygame.Rect constructors as args
    #Will return the list with the Rect constructors converted to Rect objects
    def getSprites(self, sprites):
        for i in range(len(sprites)):
            sprites[i] = self.sheet.subsurface(pygame.Rect(sprites[i]))
        return sprites
    
    #Load a sprite sheet into self.sheet
    def loadSheet(self, sheet):
        self.sheet = pygame.image.load("./assets/sprites/" + sheet + ".png")
        
    #Return a scaled image multiplied to the scale constant
    def scaleImage(self, image):
        self.SCALE = 5
        return pygame.transform.scale(image, (image.get_rect().width * self.SCALE, image.get_rect().height * self.SCALE))