import pygame, yaml

class SpriteProvider:
    def __init__(self):
        self.SCALE = yaml.safe_load(open("./settings.yaml"))["scale"] #Scale constant
    def getSprites(self, sprites: list):
        """
        Takes in a list with pygame.Rect constructors as args
        Will return the list with the Rect constructors converted to Rect objects
        """
        images = []
        for i in range(len(sprites)):
            images.append(self.sheet.subsurface(pygame.Rect(sprites[i])))
        return images
    
    def loadSheet(self, sheet: str):
        """
        Load a sprite sheet into self.sheet
        """
        self.sheet = pygame.image.load("./assets/sprites/" + sheet + ".png")
        
    def scaleImage(self, image: pygame.surface.Surface):
        """
        Scale an image to the scale constant
        """
        return pygame.transform.scale(image, (image.get_rect().width * self.SCALE, image.get_rect().height * self.SCALE))