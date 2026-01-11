import pygame
from entities.spriteProvider import SpriteProvider

class Entity:
    def __init__(self, screen):
        self.screen = screen #Define screen for drawing
        self.sp = SpriteProvider()
        self.SPEED = 10 #Speed constant
        self.rect = pygame.Rect(0, 0, 16, 16) #Coordinates and hitbox size
    
    def checkCollision(self, pos1, pos2=None):
        pygame.draw.line(self.screen.screen, (0, 0, 0), pos1, pos2)
        pos1 = ((pos1[0] // (16 * self.screen.SCALE))-1, (pos1[1] // (16 * self.screen.SCALE))-1)
        for tile in self.screen.tm.map[pos1[0]][pos1[1]]:
            if tile.hasCollision:
                pos1 = True
        if pos2 != None:
            pos2 = ((pos2[0] // (16 * self.screen.SCALE))-1, (pos2[1] // (16 * self.screen.SCALE))-1)
            for tile in self.screen.tm.map[pos2[0]][pos2[1]]:
                if tile.hasCollision:
                    pos2 = True
        return bool(pos1 == True or pos2 == True)
