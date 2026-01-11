import pygame
from entities.entity import Entity

class player(Entity):
    def __init__(self, screen):
        Entity.__init__(self, screen)
        #Attempt to load player sprites
        try:
            self.sp.loadSheet("player/spritesheet")
            self.down = self.sp.getSprites([(0, 16, 16, 16), (17, 16, 16, 16)])
            self.down[0] = self.sp.scaleImage(self.down[0])
            self.down[1] = self.sp.scaleImage(self.down[1])
            self.left = self.sp.getSprites([(34, 16, 16, 16), (51, 16, 16, 16)])
            self.left[0] = self.sp.scaleImage(self.left[0])
            self.left[1] = self.sp.scaleImage(self.left[1])
            self.right = self.sp.getSprites([(68, 16, 16, 16), (85, 16, 16, 16)])
            self.right[0] = self.sp.scaleImage(self.right[0])
            self.right[1] = self.sp.scaleImage(self.right[1])
            self.up = self.sp.getSprites([(102, 16, 16, 16), (119, 16, 16, 16)])
            self.up[0] = self.sp.scaleImage(self.up[0])
            self.up[1] = self.sp.scaleImage(self.up[1])
        except:
            raise Exception("Failed to load player sprites")

        self.image = self.down[0] #Default sprite
        self.hitbox = (-8, 16, 16, 16)
        #Set default coordinates to middle of the screen
        self.rect.x, self.rect.y = (self.screen.width//2) - (self.image.get_rect().width//2), (self.screen.height//2) - (self.image.get_rect().height//2)
        self.direction = "down" #Default direction
        self.spriteCounter = 0 #Time since last sprite change
        self.spriteNum = 1 #Sprite index
        self.spriteTime = 7 #Time between sprite changes
    
    def updateSprite(self):
        keys = pygame.key.get_pressed() #List of booleans that represent keys pressed
        #Booleans for directional keys
        self.upPressed = bool(keys[pygame.K_w] or keys[pygame.K_UP])
        self.leftPressed = bool(keys[pygame.K_a] or keys[pygame.K_LEFT])
        self.downPressed = bool(keys[pygame.K_s] or keys[pygame.K_DOWN])
        self.rightPressed = bool(keys[pygame.K_d] or keys[pygame.K_RIGHT])
        self.collided = False
        #Set self.direction based on keys pressed
        if self.upPressed: 
            if bool(self.checkCollision((self.rect.x, self.rect.y+self.hitbox[0])) or self.checkCollision((self.rect.x+16, self.rect.y+self.hitbox[0]))): self.collided = True
            self.direction = "up"
        if self.leftPressed: 
            if bool(self.checkCollision((self.rect.x, self.rect.y+self.hitbox[0])) or self.checkCollision((self.rect.x, self.rect.y+self.hitbox[1]))): self.collided = True
            self.direction = "left"
        if self.downPressed: 
            if bool(self.checkCollision((self.rect.x, self.rect.y+self.hitbox[2])) or self.checkCollision((self.rect.x+self.hitbox[1], self.rect.y+self.hitbox[2]))): self.collided = True
            self.direction = "down"
        if self.rightPressed: 
            if bool(self.checkCollision((self.rect.x+self.hitbox[1], self.rect.y+self.hitbox[0])) or self.checkCollision((self.rect.x+self.hitbox[1], self.rect.y+self.hitbox[2]))): self.collided = True
            self.direction = "right"
        #Increment spriteCounter if a direction key is pressed
        if (self.upPressed or self.leftPressed or self.downPressed or self.rightPressed) and not self.collided:
            self.spriteCounter += 1
            if self.spriteCounter > self.spriteTime:
                if self.spriteNum == 1:
                    self.spriteNum = 2
                elif self.spriteNum == 2:
                    self.spriteNum = 1
                self.spriteCounter = 0

        #Move and draw player
        self.updatePos()
        self.drawSprite()
        
    def updatePos(self):
        #Move player based on speed constant
        if self.upPressed and not self.collided: self.rect.y -= self.SPEED
        if self.leftPressed and not self.collided: self.rect.x -= self.SPEED
        if self.downPressed and not self.collided: self.rect.y += self.SPEED
        if self.rightPressed and not self.collided: self.rect.x += self.SPEED
        
    def drawSprite(self):
        #Draw image based on direction and sprite index
        self.image = eval("self."+self.direction+str([self.spriteNum-1]))
        self.screen.screen.blit(self.image, self.rect)