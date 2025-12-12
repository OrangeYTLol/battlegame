import pygame

class player:
    def __init__(self, battle):
        self.screen = battle.screen
        self.screen_rect = battle.screen.get_rect()
        try:
            self.up1 = pygame.image.load("./sprites/player/up1.png")
            self.up2 = pygame.image.load("./sprites/player/up2.png")
            self.left1 = pygame.image.load("./sprites/player/left1.png")
            self.left2 = pygame.image.load("./sprites/player/left2.png")
            self.down1 = pygame.image.load("./sprites/player/down1.png")
            self.down2 = pygame.image.load("./sprites/player/down2.png")
            self.right1 = pygame.image.load("./sprites/player/right1.png")
            self.right2 = pygame.image.load("./sprites/player/right2.png")
        except:
            raise Exception("Failed to load player sprites")
        self.image = self.down1
        self.rect = self.image.get_rect()
        #self.rect.mid = self.screen_rect.mid
        self.direction = "down"
        self.spriteCounter = 0
        self.spriteNum = 1
        self.spriteTime = 7
    
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
        self.image = eval("self."+str(self.direction)+str(self.spriteNum))
        self.screen.blit(self.image, self.rect)
        