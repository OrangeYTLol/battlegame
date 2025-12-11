import pygame

class player:
    def __init__(self, battle):
        self.screen = battle.screen
        self.screen_rect = battle.screen.get_rect()
        self.rect = self.image.get_rect()
        self.rect.mid = self.screen_rect.mid
        self.image = None
        try:
            self.up1 = pygame.image.load("./sprites/player/up1.png")
            self.up2 = pygame.image.load("./sprites/player/up2.png")
            self.left1 = pygame.image.load("./sprites/player/left1.png")
            self.left2 = pygame.image.load("./sprites/player/left2.png")
            self.down1 = pygame.image.load("./sprites/player/down1.png")
            self.down2 = pygame.image.load("./sprites/player/down2.png")
            self.right1 = pygame.image.load("./sprites/player/right1.png")
            self.right2 = pygame.image.load("./sprites/player/right2.png")
            self.direction = "down"
        except:
            raise Exception("Failed to load player sprites")

    def updateSprite(self):
        pass