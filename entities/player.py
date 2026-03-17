import pygame
from entities.entity import Entity

class Player(Entity):
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
            raise Exception("ImageError: Failed to load player sprites")
        self.image = self.down[0] #Default sprite
        #Hitbox offsets
        self.hitbox = (8*screen.SCALE, 16*screen.SCALE, 16*screen.SCALE, 16*screen.SCALE)
        #Set default coordinates to middle of the screen
        self.pos.x, self.pos.y = (self.screen.width//2) - (self.image.get_rect().width//2), (self.screen.height//2) - (self.image.get_rect().height//2)
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
        self.direction = "down" #Default direction
        self.spriteCounter = 0 #Time since last sprite change
        self.spriteNum = 1 #Sprite index
        self.spriteTime = 7 #Time between sprite changes
    
    def update(self):
        """
        Updates the player's position and sprite every frame
        """
        keys = pygame.key.get_pressed() #List of booleans that represent keys pressed
        #Booleans for directional keys
        self.upPressed = keys[pygame.K_w] or keys[pygame.K_UP]
        self.leftPressed = keys[pygame.K_a] or keys[pygame.K_LEFT]
        self.downPressed = keys[pygame.K_s] or keys[pygame.K_DOWN]
        self.rightPressed = keys[pygame.K_d] or keys[pygame.K_RIGHT]
        #Set self.direction and change velocity based on keys pressed
        if self.upPressed: 
            self.velocity.y -= 1
            self.direction = "up"
        if self.leftPressed: 
            self.velocity.x -= 1
            self.direction = "left"
        if self.downPressed: 
            self.velocity.y += 1
            self.direction = "down"
        if self.rightPressed: 
            self.velocity.x += 1
            self.direction = "right"
        #If a direction key is pressed, increment the sprite's local time
        if self.upPressed or self.leftPressed or self.downPressed or self.rightPressed:
            self.spriteCounter += 1
            #If the sprite's local time matches the time when the sprite should update, change the sprite
            if self.spriteCounter > self.spriteTime:
                #If the sprite number is equal to the amount of sprites available, the sprite number gets reset; Else, the sprite number gets incremented by 1
                if self.spriteNum < len(eval("self."+self.direction)):
                    self.spriteNum += 1
                else:
                    self.spriteNum = 1
                self.spriteCounter = 1  

        #Move and draw player
        self.updatePos()
        self.drawSprite()
        
    def updatePos(self):
        """
        Use self.velocity to move the player if it doesn't result in a collision
        """
        #Check for a collision on a full step in the x axis; If a collision is found, check for a collision in a half step
        if not self.checkCollision(pygame.Rect(self.rect.left + self.velocity.x * self.SPEED, self.rect.top, self.rect.width, self.rect.height)):
            self.pos.x += self.velocity.x * self.SPEED
        elif not self.checkCollision(pygame.Rect(self.rect.left + self.velocity.x * self.SPEED * 0.5, self.rect.top, self.rect.width, self.rect.height)):
            self.pos.x += self.velocity.x * self.SPEED * 0.5
        #Check for a collision on a full step in the y axis; If a collision is found, check for a collision in a half step
        if not self.checkCollision(pygame.Rect(self.rect.left, self.rect.top + self.velocity.y * self.SPEED, self.rect.width, self.rect.height)):
            self.pos.y += self.velocity.y * self.SPEED
        elif not self.checkCollision(pygame.Rect(self.rect.left, self.rect.top + self.velocity.y * self.SPEED * 0.5, self.rect.width, self.rect.height)):
            self.pos.y += self.velocity.y * self.SPEED * 0.5
        self.rect.x, self.rect.y = self.pos.x, self.pos.y #Update player rectangle x and y to the new position
        self.velocity.update(0, 0) #Reset velocity in the x and y axis

    def drawSprite(self):
        """
        Draw an image to the screen based on position and current sprite
        """
        #Update self.image based on direction and sprite number
        self.image = eval("self."+self.direction+str([self.spriteNum-1]))
        #Draw the updated image to the screen with the player's updated coordinates
        self.screen.screen.blit(self.image, self.rect)