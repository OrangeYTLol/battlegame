from entities.trigger import Trigger

class upLevelTrigger(Trigger):
    def __init__(self, screen):
        super().__init__(screen)
        self.rect.x, self.rect.y = 80 * 5.5, 0
        self.rect.height *= 0.5
    
    def whenCollided(self):
        self.screen.tm.loadMap("u1")
        self.screen.player1.pos.y = 80 * 6.5 - 10

class leftLevelTrigger(Trigger):
    def __init__(self, screen):
        super().__init__(screen)
        self.rect.x, self.rect.y = 0, 80 * 3.5
        self.rect.width *= 0.5
    
    def whenCollided(self):
        self.screen.tm.loadMap("l1")
        self.screen.player1.pos.x = 80 * 10.5 - 10

class rightLevelTrigger(Trigger):
    def __init__(self, screen):
        super().__init__(screen)
        self.rect.x, self.rect.y = 80 * 11.5, 80 * 3.5
        self.rect.width *= 0.5
    
    def whenCollided(self):
        self.screen.tm.loadMap("r1")
        self.screen.player1.pos.x = 80 * 0.5 + 10

class downLevelTrigger(Trigger):
    def __init__(self, screen):
        super().__init__(screen)
        self.rect.x, self.rect.y = 80 * 4.5, 80 * 7.5
        self.rect.width *= 3
        self.rect.height *= 0.5
    
    def whenCollided(self):
        self.screen.tm.loadMap("d1")
        self.screen.player1.pos.y = 80 * 0.5 + 10