from entities.trigger import Trigger

class upLevelTrigger(Trigger):
    def __init__(self, screen):
        super().__init__(screen)
        self.rect.x, self.rect.y = 80 * 4.5, 0
        self.rect.width *= 3
        self.rect.height *= 0.5
    
    def whenCollided(self):
        self.screen.tm.loadMap("start")
        self.screen.player1.pos.y = 80 * 6.5