import pygame
from entities.spriteProvider import SpriteProvider

class Entity:
    def __init__(self, screen):
        self.screen = screen
        self.sp = SpriteProvider()
        self.SPEED = 5
        self.rect = pygame.Rect(0, 0, 16, 16)