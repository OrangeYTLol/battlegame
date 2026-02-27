from entities.trigger import Trigger

class leftLevelTrigger(Trigger):
    def __init__(self, screen):
        super().__init__(screen)
        self.rect.x, self.rect.y = 0, 80 * 3.5
        self.rect.width *= 0.5
    
    def whenCollided(self):
        self.screen.tm.loadMap("start")
        self.screen.player1.pos.x = 80 * 10.5 - 10