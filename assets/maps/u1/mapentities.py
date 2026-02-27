from entities.trigger import Trigger

class downLevelTrigger(Trigger):
    def __init__(self, screen):
        super().__init__(screen)
        self.rect.x, self.rect.y = 80 * 5.5, 80 * 7.5
        self.rect.height *= 0.5
    
    def whenCollided(self):
        self.screen.tm.loadMap("start")
        self.screen.player1.pos.y = 80 * 0.5 + 10