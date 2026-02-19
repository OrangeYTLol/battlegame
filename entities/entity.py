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
        self.rect = pygame.Rect(0, 0, 16 * self.sp.SCALE, 16 * self.sp.SCALE) #Coordinates and hitbox size
    
    def checkCollision(self, rect):
        """
        Return true if given rectangle collides with list of tiles with collision
        """
        return rect.collidelist(self.screen.tm.collision_group) != -1
