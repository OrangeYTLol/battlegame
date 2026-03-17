from entities.entity import Entity
class Trigger(Entity):
    def __init__(self, screen):
        super().__init__(screen)
        self.image = self.sp.getSprites([(0, 0, 1, 1)])[0]
    
    def whenCollided(self):
        """
        Generic function that gets triggered when a collision between the player and the trigger occurs; should be overriden by child classes
        """
        pass

    def playerCollided(self):
        """
        Checks if the trigger has collided with the player
        """
        return self.rect.colliderect(self.screen.player1)
    
    def update(self):
        super().update()
        #Run a function when trigger collides with the player
        if self.playerCollided():
            self.whenCollided()