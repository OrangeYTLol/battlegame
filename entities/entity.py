import pygame
from spriteProvider import SpriteProvider

class Entity:
    def __init__(self, screen):
        self.screen = screen
        self.sp = SpriteProvider()
        self.SPEED = 5
        self.rect = pygame.Rect(0, 0, 16, 16)
    
    def scaleImage(self, image):
        SCALE = 4
        return pygame.transform.scale(image, (image.get_rect().width * SCALE, image.get_rect().height * SCALE))