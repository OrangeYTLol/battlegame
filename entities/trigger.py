from entities.entity import Entity
class Trigger(Entity):
    def __init__(self, screen):
        super().__init__(screen)
        self.image = self.sp.getSprites([(0, 0, 1, 1)])[0]
    
    def whenCollided(self):
        pass

    def playerCollided(self):
        return self.rect.colliderect(self.screen.player1)
    
    def update(self):
        super().update()
        if self.playerCollided():
            self.whenCollided()
        