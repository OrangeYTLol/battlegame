import pygame
from entities.spriteProvider import SpriteProvider

class Entity:
    def __init__(self, screen):
        self.screen = screen #Define screen for drawing
        self.sp = SpriteProvider()
        self.SPEED = 10 #Speed constant
        #Position and velocity
        self.pos = pygame.math.Vector2()
        self.velocity = pygame.math.Vector2()
        self.sp.loadSheet("player/spritesheet")
        self.image = self.sp.scaleImage(self.sp.getSprites([(0, 16, 16, 16)])[0])
        self.rect = pygame.Rect(0, 0, 16 * self.sp.SCALE, 16 * self.sp.SCALE) #Coordinates and hitbox size
    
    def checkCollision(self, rect: pygame.Rect):
        """
        Check if the given rectangle collides with the list of tiles with collision
        """
        return rect.collidelist(self.screen.tm.collision_group) != -1

    def drawSprite(self):
        """
        Draw self.image to the screen
        """
        self.screen.screen.blit(self.image, self.rect)
    
    def update(self):
        """
        Generic update function meant to be overriden by child classes, draws the sprite to the screen on every frame 
        """
        self.drawSprite()