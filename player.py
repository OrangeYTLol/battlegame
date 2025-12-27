import pygame.key
from spriteProvider import SpriteProvider

class player:
    def __init__(self, battle):
        self.screen = battle.screen
        self.screen_rect = battle.screen.get_rect()
        sp = SpriteProvider("player/spritesheet")
        try:
            self.down = sp.getSprites([(0, 16, 16, 16), (17, 16, 16, 16)])
            self.left = sp.getSprites([(34, 16, 16, 16), (51, 16, 16, 16)])
            self.right = sp.getSprites([(68, 16, 16, 16), (85, 16, 16, 16)])
            self.up = sp.getSprites([(102, 16, 16, 16), (119, 16, 16, 16)])
        except:
            raise Exception("Failed to load player sprites")
        self.image = self.down[0]
        self.rect = self.image.get_rect()
        #self.rect.mid = self.screen_rect.mid
        self.direction = "down"
        self.spriteCounter = 0
        self.spriteNum = 1
        self.spriteTime = 3
    
    def updateSprite(self):
        keys = pygame.key.get_pressed()
        self.upPressed = bool(keys[pygame.K_w] or keys[pygame.K_UP])
        self.leftPressed = bool(keys[pygame.K_a] or keys[pygame.K_LEFT])
        self.downPressed = bool(keys[pygame.K_s] or keys[pygame.K_DOWN])
        self.rightPressed = bool(keys[pygame.K_d] or keys[pygame.K_RIGHT])
        if self.upPressed: self.direction = "up"
        if self.leftPressed: self.direction = "left"
        if self.downPressed: self.direction = "down"
        if self.rightPressed: self.direction = "right"
        
        if (self.upPressed or self.leftPressed or self.downPressed or self.rightPressed):
            self.spriteCounter += 1
            if self.spriteCounter > self.spriteTime:
                if self.spriteNum == 1:
                    self.spriteNum = 2
                elif self.spriteNum == 2:
                    self.spriteNum = 1
                self.spriteCounter = 0
                
        self.drawSprite()
        
    def drawSprite(self):
        self.image = eval("self."+self.direction+str([self.spriteNum-1]))
        self.rect = self.image.get_rect()
        self.screen.blit(self.image, self.rect)
        