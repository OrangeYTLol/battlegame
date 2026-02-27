from entities.trigger import Trigger

class rightLevelTrigger(Trigger):
    def __init__(self, screen):
        super().__init__(screen)
        self.rect.x, self.rect.y = 80 * 11.5, 80 * 3.5
        self.rect.width *= 0.5
    
    def whenCollided(self):
        self.screen.tm.loadMap("start")
        self.screen.player1.pos.x = 80 * 0.5 + 10