import pygame
from entities.spriteProvider import SpriteProvider

class Entity:
    def __init__(self, screen):
        self.screen = screen #Define screen for drawing
        self.sp = SpriteProvider()
        self.SPEED = 10 #Speed constant
        self.rect = pygame.Rect(0, 0, 16, 16) #Coordinates and hitbox size
    
    def checkCollision(self, position):
        print(position)
        position = (position[0] // (16 * self.screen.SCALE), position[1] // (16 * self.screen.SCALE))
        for tile in self.screen.tm.map[position[0]][position[1]]:
            if tile.hasCollision:
                return True
        return False