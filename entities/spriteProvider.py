import pygame

class SpriteProvider:
    def __init__(self):
        self.SCALE = 5 #Scale constant
    def getSprites(self, sprites: list):
        """
        Takes in a list with pygame.Rect constructors as args
        Will return the list with the Rect constructors converted to Rect objects
        """
        images = []
        for i in range(len(sprites)):
            images.append(self.sheet.subsurface(pygame.Rect(sprites[i])))
        return images
    
    #Load a sprite sheet into self.sheet
    def loadSheet(self, sheet: str):
        self.sheet = pygame.image.load("./assets/sprites/" + sheet + ".png")
        
    #Return a scaled image multiplied to the scale constant
    def scaleImage(self, image: pygame.surface.Surface):
        """
        Takes an image and multiplies it using the scale constant
        """
        
        self.SCALE = 5
        return pygame.transform.scale(image, (image.get_rect().width * self.SCALE, image.get_rect().height * self.SCALE))